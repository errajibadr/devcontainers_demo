from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.tasks.worker import process_data, stock_data, test_task

app = FastAPI(title="DataPilot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Bienvenue sur DataPilot API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/tasks/test")
async def create_test_task(seconds: int = 10):
    task = test_task.delay(seconds)
    return {"task_id": task.id}


@app.get("/tasks/status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None,
    }
    return result


@app.post("/tasks/process")
async def create_process_task(data: dict):
    task = process_data.delay(data)
    return {"task_id": task.id}


@app.get("/tasks/fetch_stock_data/{symbol}")
async def fetch_stock_data(symbol: str):
    task = stock_data.delay(symbol)
    return {"task_id": task.id}
