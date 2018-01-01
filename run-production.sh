#!/bin/bash

MEDICI_SERVER=medici_server

PROJECT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
STATIC_DIR="/srv/http/static"
MEDIA_DIR="/srv/http/media"

templates=("nginx_template.conf" "uwsgi_template.ini" "settings_template.py")
configs=("nginx.conf" "uwsgi.ini" "settings.py")
counter=0
for template in ${templates[@]}
do
    config=${configs[$counter]}

    content=$(cat $PROJECT_DIR/$MEDICI_SERVER/$template | sed "s~<project_dir>~$PROJECT_DIR~g")
    echo "$content" >$PROJECT_DIR/$MEDICI_SERVER/$config

    content=$(cat $PROJECT_DIR/$MEDICI_SERVER/$config | sed "s~<static_dir>~$STATIC_DIR~g")
    echo "$content" >$PROJECT_DIR/$MEDICI_SERVER/$config

    content=$(cat $PROJECT_DIR/$MEDICI_SERVER/$config | sed "s~<media_dir>~$MEDIA_DIR~g")
    echo "$content" >$PROJECT_DIR/$MEDICI_SERVER/$config

    ((counter++))
done;

sudo python manage.py collectstatic

sudo systemctl start nginx
uwsgi --ini $MEDICI_SERVER/uwsgi.ini
