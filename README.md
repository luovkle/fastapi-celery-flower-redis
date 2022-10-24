# fastapi-celery-flower-rabbitmq

This repository is intended to show an example of how to connect fastapi with celery and flower, in docker containers.

## Requirements

- git
- docker
- docker-compose

## Running servers

```sh
git clone https://github.com/luovkle/fastapi-celery-flower-rabbitmq
cd fastapi-celery-flower-rabbitmq
docker-compose up -d
```

## Accessing services

To access the services you have to access the following addresses from your web browser.

- **fastapi:** localhost:8000
- **flower:** localhost:5555
- **rabbitmq:** localhost:15672

The username and password for rabbitmq are **guest** for both fields.
