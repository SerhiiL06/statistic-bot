from datetime import datetime
from random import randint
import asyncio
import aiosqlite


async def get_job_count() -> dict:

    job_count = {"timestamp": datetime.now(), "job_count": randint(1, 5)}
    return job_count


async def save_to_db(timestamp, job_count):

    async with aiosqlite.connect("db.sqlite3") as connect:

        await connect.execute(
            """CREATE TABLE IF NOT EXISTS job_counts
                    (timestamp TEXT, job_count INTEGER)"""
        )

        await connect.execute(
            "INSERT INTO job_counts (timestamp, job_count) VALUES (?, ?)",
            (timestamp, job_count),
        )
        await connect.commit()
        await connect.close()


async def main():
    job_count = await get_job_count()

    await save_to_db(job_count.get("timestamp"), job_count.get("job_count"))


if __name__ == "__main__":
    asyncio.run(main())
