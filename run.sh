#!/bin/bash

echo "Запуск Telegram-бота..."
python bot.py &
BOT_PID=$!

echo "Запуск Redis..."
redis-server & REDIS_PID=$!

echo "Запуск Celery worker..."
celery -A core.celery.app worker -B -l INFO &
CELERY_PID=$!

cleanup() {
    echo "Зупинка Telegram-бота і Celery worker..."
    kill $BOT_PID
    kill $REDIS_PID
    kill $CELERY_PID
    wait $BOT_PID
    wait $REDIS_PID
    wait $CELERY_PID
    echo "Всі процеси зупинено."
}

trap cleanup SIGINT SIGTERM


wait $BOT_PID
wait $REDIS_PID
wait $CELERY_PID