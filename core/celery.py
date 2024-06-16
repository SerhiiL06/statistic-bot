from celery import Celery

app = Celery(
    "statictic",
    broker="redis://localhost",
    backend="redis://localhost",
    include=["src.task.logic"],
)


app.conf.beat_schedule = {
    "first_schedule": {
        "task": "src.task.logic.parse_and_save",
        "schedule": 30,
    },
}
