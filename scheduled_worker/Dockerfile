FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /schedule

WORKDIR /schedule

COPY . /schedule/

RUN pip install -r requirements.txt