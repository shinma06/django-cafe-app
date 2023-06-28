FROM python:3.11.4

RUN apt-get update

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip
RUN pip install django mysqlclient pillow