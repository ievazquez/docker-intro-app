# build
FROM golang:alpine as builder

RUN apk update && \
  apk add --no-cache git ca-certificates tzdata \
  # && apk add --no-cache curl \
  && update-ca-certificates


# Move to working directory /build
WORKDIR /app

# Copy go.mod & go.sum, run go mod download
COPY go.mod go.sum ./
RUN go mod download

# Copy the code into the container
COPY . .

# Download dependency using go mod
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o main .




