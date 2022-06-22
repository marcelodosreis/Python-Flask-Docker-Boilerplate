# Python Boilerplate

## Technologies
- Python
- Flask
- SQLAlchemy
- PostgresSQL
- Docker

## Base Setup
- Install setup `. install.sh`


## Installation of the necessary “packages”.
- Docker → [Docker Installation Tutorial](https://docs.docker.com/engine/install/ubuntu/)
- Docker compose → [docker-compose Installation Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-pt)

## Start Project
_Docker is configured to raise two containers, the flask application image and the postgres database. For more details see the **docker-compose.yml** configuration file_
```
docker-compose up --build
```


## Environment variables
_You need create .env file, use .env.example file for template_
```
DATABASE_HOST=
DATABASE_PORT=

POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```