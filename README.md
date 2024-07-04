# Django Celery Example

This is a simple example of how to use Celery with Django. In my code I use RabbitMQ as a broker and Redis as a backend.

This code is really nice if you want to understand how Celery works with Django. Also, you can use it to learn how to
deploy such projects using Docker.

## How to run

Simply clone this repository and run the following commands:

```bash
docker-compose build
docker-compose up
```

__Note__: *You need to have Docker and Docker Compose installed on your machine.*

__Note 2__: *Don't forget to rename .env-example to .env, otherwise this code won't work*

## How to test

Run the following command:

```bash
docker-compose run web python manage.py test
```