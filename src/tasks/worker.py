import os
import time
from datetime import datetime, timedelta

import yfinance as yf
from celery import Celery

redis_host = os.getenv("REDIS_HOST", "localhost")
celery_app = Celery(
    "tasks",
    broker=f"redis://{redis_host}:6379/0",
    backend=f"redis://{redis_host}:6379/0",
    include=["src.tasks.worker"],
)

# Optional configurations
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task(name="test_task")
def test_task(seconds: int = 10):
    time.sleep(seconds)  # Simulate long running task
    return {"status": "completed", "message": f"Task completed after {seconds} seconds"}


@celery_app.task(name="process_data")
def process_data(data: dict):
    # Example task that processes some data
    result = {"processed": data}
    return result


@celery_app.task(name="stock_data")
def stock_data(symbol: str):
    """Récupère les données boursières pour un symbole donné."""
    stock = yf.Ticker(symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    hist = stock.history(start=start_date, end=end_date)
    return hist.to_dict()
