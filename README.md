# fastapi-celery-flower-redis

This repository is intended to show an example of how to connect fastapi with celery and flower, in docker containers.

## Requirements

- git
- docker
- docker-compose

## Running servers

```sh
git clone https://github.com/luovkle/fastapi-celery-flower-redis
cd fastapi-celery-flower-redis
docker-compose up -d
```

## Accessing services

To access the services you have to access the following addresses from your web browser.

- **fastapi:** localhost:8000
- **flower:** localhost:5555
