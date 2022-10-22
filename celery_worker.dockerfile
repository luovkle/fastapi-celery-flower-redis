FROM python:alpine
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN pip install $(cat requirements.txt | grep celery)
COPY ["celery_worker.py", "/app/"]
CMD ["celery", "-A", "celery_worker.celery", "worker", "--loglevel=info"]
