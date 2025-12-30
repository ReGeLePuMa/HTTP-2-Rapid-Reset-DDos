FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    iproute2 \
    curl

WORKDIR /app
COPY  ./app/ .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
