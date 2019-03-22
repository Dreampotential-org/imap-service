#!/bin/bash

python3 manage.py sync_accounts

exec "$@"
