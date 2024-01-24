# Use the official Python image with version 3.10
# FROM ubuntu:latest
FROM python:3.10-slim-buster

# FROM python:3.10.0a6-alpine3.13
# Install build dependencies
RUN apt update && apt install -y build-essential

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt


CMD ["uwsgi", "app.ini", "--thunder-lock"]
