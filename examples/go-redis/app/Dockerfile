# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# Start from golang:1.12-alpine base image
FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod go.sum /app

RUN go mod download

COPY . .

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]

