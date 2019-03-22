#!/bin/bash

# exit immediately on failure, or if an undefined variable is used
set -eu

docker exec -it imap-server_mail-api_1  ./scripts/sync_imap_accounts.sh

exec "$@"
