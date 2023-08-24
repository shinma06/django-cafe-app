#!/bin/bash

set -e

# management/commands/runcontainer.py参照
cmd="python3 manage.py runcontainer"

until nc -z mysql 3306; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - starting server"

# Infinite loop to restart server if it crashes
while true; do
    $cmd || {
        echo "Server crashed. Restarting in 5 seconds..."
        sleep 5
    }
done
