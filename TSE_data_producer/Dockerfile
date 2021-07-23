FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /TSE_producer

WORKDIR /TSE_producer

COPY . /TSE_producer/

RUN pip install -r requirements.txt