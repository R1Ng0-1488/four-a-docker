#!/bin/sh

echo "dick"
if [ "$DATABASE" = "postgres" ]
then
	echo "Waiting for postgres..."
	sleep 5
	while ! nc -z $SQL_HOST $SQL_PORT; do
	  sleep 0.1
	done
	
	echo "PosqtgreSQL started"

fi 

python manage.py flush --no-input
# python manage.py makemigrations
python manage.py migrate

exec "$@"

sleep 10