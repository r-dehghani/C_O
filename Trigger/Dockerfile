FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /trigger

WORKDIR /trigger

COPY . /trigger/

RUN pip install -r requirements.txt