import sqlite3
from datetime import datetime
from random import randint

from celery import shared_task


def get_job_count() -> dict:

    job_count = {
        "timestamp": datetime.now(),
        "job_count": randint(1, 5),
    }
    return job_count


def save(timestamp, job_count):

    sq = sqlite3.connect("db.sqlite3")

    sq.execute(
        """CREATE TABLE IF NOT EXISTS job_counts
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, check_date DATE, job_count INTEGER)"""
    )

    sq.execute(
        "INSERT INTO job_counts (check_date, job_count) VALUES (?, ?)",
        (timestamp, job_count),
    )
    sq.commit()
    sq.close()


@shared_task
def parse_and_save():

    count = get_job_count()

    save(count.get("timestamp"), count.get("job_count"))
