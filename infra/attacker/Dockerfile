FROM golang:1.24.1-alpine as builder

WORKDIR /app
COPY . .
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
RUN go get . && \
    go build -o attacker

FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    iproute2 \
    curl

WORKDIR /attacker

COPY --from=builder /app/attacker ./attacker
