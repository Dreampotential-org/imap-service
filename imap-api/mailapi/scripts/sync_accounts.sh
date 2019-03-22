#!/bin/bash

# syncs mail account

python3 manage.py sync_accounts

exec "$@"
