FROM golang:1.10 as go_builder

RUN mkdir -p /opt/workspace/app
COPY app /opt/workspace/app
ENV GOPATH /opt/workspace/app
WORKDIR /opt/workspace/app
RUN go build sample.go

#Need to copy only binary
FROM alpine:3.7
WORKDIR /opt/workspace
COPY --from=go_builder /opt/workspace/app/sample /opt/workspace/ankur
RUN chmod 777 ankur
ENTRYPOINT ./ankur 
