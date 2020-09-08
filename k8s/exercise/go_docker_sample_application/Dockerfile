FROM alpine:3.7
FROM golang:1.10 as go
RUN go build sample.go
RUN mkdir -p /opt/workspace
COPY go_docker_sample_application /opt/workspace
WORKDIR /opt/workspace
RUN chmod 777 go_docker_sample_application
ENTRYPOINT ./go_docker_sample_application 
