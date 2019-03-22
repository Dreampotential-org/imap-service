#!/bin/bash

# exit immediately on failure, or if an undefined variable is used
set -eu

docker-compose down
docker-compose build
docker-compose up -d
cd docker-mailserver
docker-compose build
docker-compose up -d mail && rm -rf /opt/var/mail-api.ciimbre.com/static/*
cp -R ../imap-api/mailapi/static/* /opt/var/mail-api.ciimbre.com/static/

exec "$@"
