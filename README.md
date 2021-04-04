# aeroplane

An experiment combining [Django](https://www.djangoproject.com/), [Pydantic-Django](https://github.com/jordaneremieff/pydantic-django), and [FastAPI](https://fastapi.tiangolo.com/).

<img width="400" alt="Screen Shot 2021-04-04 at 1 21 41 am" src="https://user-images.githubusercontent.com/1376648/113481348-b54b5700-94e4-11eb-8eb8-988d4cfc5020.png"> <img width="400" alt="Screen Shot 2021-04-04 at 1 22 07 am" src="https://user-images.githubusercontent.com/1376648/113481353-cbf1ae00-94e4-11eb-90b2-75d8b3ca7b6c.png">

## Initial setup

First create a virtual environment and install the dependencies:

```shell
python -m .venv venv
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

Run the server locally using `uvicorn`:

```shell
uvicorn aeroplane.main:app --debug
```

The [auto-generated docs](https://fastapi.tiangolo.com/features/#automatic-docs) proivded by FastAPI are available at http://localhost:8000/docs

The [model admin](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) provided by Django is availabe at http://localhost:8000/dj/admin

## Deploying to AWS Lambda & API Gateway

This example provides a configuration for using [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) with [Mangum](https://mangum.io) to deploy the ASGI application to AWS Lambda with API Gateway, and it requires a remote Postgres database to be configured in the application settings.

The following steps assumes a remote Postgres database is already setup and Serverless Framework is already installed:

- Edit the `serverless.yml` where necessary
- Add the remote database details to `.env`
- Run `sls deploy`
