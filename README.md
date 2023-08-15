# fastapi-celery-flower-redis

This repository provides a practical demonstration of integrating FastAPI with Celery and Redis within Docker containers.

The example showcases a simulated process of sending fictitious emails through a FastAPI-powered REST API. The asynchronous queue management of Celery ensures smooth operation, with email sending taking 1 to 4 seconds.

## Requirements

To successfully run and understand this example, ensure you have the following components installed:

- **Git**
- **Docker Compose** (version 19.03.0+)

## Running

Follow these steps to run the example on your local machine:

1. Clone the repository:

```sh
git clone https://github.com/luovkle/fastapi-celery-flower-redis.git
cd fastapi-celery-flower-redis
```

2. Build and start the Docker containers using Docker Compose:

```sh
docker compose up -d
```

3. Allow the containers to initialize. The FastAPI application, Celery workers, and Redis services should all become active.

## Accessing Services

Once the containers are up, you can access the following services:

- **FastAPI** REST API: Access the FastAPI application by navigating to **http://localhost:8000** in your web browser or using tools like curl or Postman.
- **Flower** Monitoring Dashboard: Monitor the Celery tasks and workers by visiting **http://localhost:5555** in your web browser.
- **Redis**: Redis, used as both backend and broker, is accessible internally within the network.

Explore this repository's code to comprehend the integration of FastAPI, Celery, and Redis for creating an efficient asynchronous email processing system.

For queries or issues, kindly open an issue on this repository.

## Note

This example is intended for educational purposes and might not reflect a production-ready setup. Make sure to adapt it according to your needs and security considerations before deploying it in a production environment.
