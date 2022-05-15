FROM golang:latest

RUN mkdir /app

ADD . /app
COPY go.mod /app
#COPYy *.go /app

WORKDIR /app

RUN go build -o main .

CMD ["/app/main"]
