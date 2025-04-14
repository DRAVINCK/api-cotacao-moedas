FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn requests mysql-connector-python redis

EXPOSE 8000
EXPOSE 8001
