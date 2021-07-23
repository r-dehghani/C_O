FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /api

WORKDIR /api

COPY . /api/

RUN pip install -r requirements.txt