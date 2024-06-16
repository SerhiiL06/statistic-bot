import logging
import re
import sqlite3
from datetime import datetime
from typing import Optional

from celery import shared_task
from selenium import webdriver

from .driver import driver


def get_job_count(driver: webdriver.Chrome) -> Optional[dict]:

    url = "https://robota.ua/zapros/junior/ukraine"
    driver.get(url)

    page_source = driver.page_source

    driver.quit()

    pattern = re.compile(r"(\d[\d\s]+)\s+(вакансій|вакансія|вакансії)", re.IGNORECASE)
    result = pattern.search(page_source)

    if result:
        to_int = int(result.group(1).replace(" ", ""))

        job_count = {
            "timestamp": datetime.now(),
            "job_count": to_int,
        }
        return job_count


def save(timestamp, job_count) -> None:

    with sqlite3.connect("db.sqlite3") as sq:

        create_query = """CREATE TABLE IF NOT EXISTS job_counts
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, check_date DATE, job_count INTEGER)"""
        sq.execute(create_query)

        insert_query = "INSERT INTO job_counts (check_date, job_count) VALUES (?, ?)"
        sq.execute(insert_query, (timestamp, job_count))

        sq.commit()


@shared_task
def parse_and_save() -> None:

    count = get_job_count(driver.instance)

    logging.info(f"Get count data: {count}")

    if count:
        save(count.get("timestamp"), count.get("job_count"))
