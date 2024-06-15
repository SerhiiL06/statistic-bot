import asyncio

from core.config import bot, dp
from src.bot.handlers import router


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
