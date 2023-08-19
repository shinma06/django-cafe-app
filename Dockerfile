FROM python:3.11.4

RUN apt-get update

RUN mkdir /cafeapp

WORKDIR /cafeapp

COPY requirements.txt ./
COPY combined_script.sh ./

RUN chmod +x combined_script.sh
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install --upgrade pip && pip install -r requirements.txt