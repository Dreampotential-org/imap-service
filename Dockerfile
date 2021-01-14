FROM ubuntu:latest
ENV PYTHONIOENCODING=utf-8
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y memcached
RUN apt-get install -y dovecot-core

COPY imap-api/req.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

COPY entrypoint.sh /entrypoint.sh

WORKDIR /home/web/codes
