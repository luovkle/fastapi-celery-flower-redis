FROM python:alpine
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN pip install -r requirements.txt
COPY ["main.py", "model.py", "celery_worker.py", "/app/"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
