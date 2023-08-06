FROM python:3.11.4

RUN apt-get update

RUN mkdir /cafeapp

WORKDIR /cafeapp

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt