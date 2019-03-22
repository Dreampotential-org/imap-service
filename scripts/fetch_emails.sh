#!/bin/bash

docker exec -it imap-server_mail-api_1  ./scripts/fetch_emails.sh

exec "$@"
