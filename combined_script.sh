#!/bin/bash

set -e

# management/commands/runcontainer.py参照
cmd="python3 manage.py runcontainer"

until nc -z mysql 3306; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
