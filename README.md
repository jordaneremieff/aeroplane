# aeroplane

An experiment combining [Django](https://www.djangoproject.com/) and [FastAPI](https://fastapi.tiangolo.com/). Also includes [Djantic](https://github.com/jordaneremieff/djantic) for converting Django models to Pydantic models and an example serverless configuration.

<p align="center">
<kbd><img width="200" alt="Screen Shot 2021-04-04 at 3 48 27 pm" src="https://user-images.githubusercontent.com/1376648/113499971-c97f6a80-955d-11eb-99b0-a81ea2344ac1.png"></kbd>
<kbd><img width="200" alt="Screen Shot 2021-04-04 at 3 47 54 pm" src="https://user-images.githubusercontent.com/1376648/113499972-cab09780-955d-11eb-9aee-3b4bad6cba08.png"></kbd>
</p>

## Initial setup

***Requirements***: Python 3.7+

First create a virtual environment and install the dependencies:

```shell
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

***Note***: The `mangum` requirement is only necessary if deploying to AWS Lambda, and `psycopg2-binary` is only necessary for Postgres support.

## Configuring the database

Any supported Django database configuration can be used, this example provides to examples:

- To use Postgres, rename `.env.dist` to `.env` and set the details for the database. These will be loaded in `settings.py`.

- To use SQLite, edit `settings.py` to uncomment the sqlite3 database configuration.

Then populate the initial database tables using the migration command:

```shell
./manage.py migrate
```

## Running the application locally

(Don't forget to) Create a Superuser:
```shell
./manage.py createsuperuser
```

Run the server locally using `uvicorn`:

```shell
uvicorn aeroplane.main:app
```

The [model admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/) provided by Django is availabe at http://localhost:8000/dj/admin


The [auto-generated docs](https://fastapi.tiangolo.com/features/#automatic-docs) provided by FastAPI are available at http://localhost:8000/docs

## Deploying to AWS Lambda & API Gateway

This example provides a configuration for using [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) with [Mangum](https://mangum.io) to deploy the ASGI application to AWS Lambda with API Gateway, and it requires a remote Postgres database to be configured in the application settings.

The following steps assumes a remote Postgres database is already setup and Serverless Framework is already installed:

- Edit the `serverless.yml` where necessary
- Add the remote database details to `.env`
- Run `sls deploy`
