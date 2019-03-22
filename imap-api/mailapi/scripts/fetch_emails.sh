#!/bin/bash

python3 manage.py fetch_mails

exec "$@"
