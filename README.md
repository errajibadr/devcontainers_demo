To start the API server, run:
```bash
uvicorn src.api.main:app --reload --port 8000 --reload-dir src 
```


To start the worker, run:
```bash
celery -A src.tasks.worker worker --loglevel=info  --autoreload
```

To monitor the worker, run:
```bash
celery -A src.tasks.worker flower
```
Then go to http://localhost:5555

