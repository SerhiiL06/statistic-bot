import sqlite3

import pandas as pd
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

router = Router(name=__name__)


@router.message(CommandStart())
async def starting(message: Message):

    await message.answer("hello from stastic bot!")


@router.message(Command("get_count"))
async def get_statistic(message: Message):

    connect = sqlite3.connect("db.sqlite3")
    query = "SELECT * FROM job_counts WHERE DATE(check_date) = DATE('now')"
    df = pd.read_sql(query, connect)
    df.to_excel("job_counts_today.xlsx")
    file = FSInputFile("job_counts_today.xlsx")

    await message.answer_document(file)
