FROM golang:1.14.6 as go_builder
RUN mkdir -p /opt/workspace/gofactor
WORKDIR /opt/workspace/gofactor
COPY . .
RUN go mod download
RUN go build

#Need to copy only binary
#FROM alpine:3.7 ----with this getting error "/bin/sh: ./gofactor: not found"
FROM ubuntu:18.04
WORKDIR /opt/workspace
COPY --from=go_builder /opt/workspace/gofactor/gofactor /opt/workspace/gofactor
RUN chmod 777 gofactor
EXPOSE 8090
ENTRYPOINT ./gofactor 
#gofactor -db-init