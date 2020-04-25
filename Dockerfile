FROM python:3.7-alpine
MAINTAINER Danny Rojas

ENV PYTHONUNBUFFERDED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /apps

RUN adduser -D user
USER user



