FROM python:3.11.4

RUN apt-get update

RUN mkdir /cafeapp

WORKDIR /cafeapp

RUN pip install --upgrade pip && \
    pip install django mysqlclient pillow