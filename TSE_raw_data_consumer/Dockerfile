FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /tse_cosumer

WORKDIR /tse_cosumer

COPY . /tse_cosumer/

RUN pip install -r requirements.txt