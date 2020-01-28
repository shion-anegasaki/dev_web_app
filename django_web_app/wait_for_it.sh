#!/bin/sh

set -e

host="$1"
shift
user="$1"
shift
password="$1"
shift
cmd="$@"

echo "Waiting for mysql"
until mysqladmin ping -h "$host" -u "$user" -p"$password" --silent &> /dev/null;
do
    echo -n "."
    sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
