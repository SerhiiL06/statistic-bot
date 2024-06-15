import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()


class Settings:
    _TELEGRAM_TOKEN = os.getenv("TOKEN")

    @property
    def token(self):
        return self._TELEGRAM_TOKEN


settings = Settings()


bot = Bot(settings.token)


dp = Dispatcher()
