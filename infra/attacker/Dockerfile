FROM golang:1.24.1-alpine as builder

WORKDIR /app
COPY . .
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
RUN go get . && \
    go build -o attacker

FROM scratch

COPY --from=builder /app/attacker /attacker

