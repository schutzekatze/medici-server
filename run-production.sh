#!/bin/bash

PROJECT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
MAIN_APP=medici_server
DOMAIN_NAME=medici.ddns.net
STATIC_DIR=/srv/http/static
MEDIA_DIR=/srv/http/media

NGINX_SERVERS_DIR=/etc/nginx/sites-enabled
SOCKET_PATH=/tmp/medici_server.sock
NGINX_USER=http

templates=("nginx_template.conf" "uwsgi_template.ini" "settings_template.py")
configs=("nginx.conf" "uwsgi.ini" "settings.py")
counter=0
for template in ${templates[@]}
do
    config=${configs[$counter]}

    content=$(cat $PROJECT_DIR/$MAIN_APP/$template)

    content=$(echo "$content" \
            | sed "s~<project_dir>~$PROJECT_DIR~g" \
            | sed "s~<main_app>~$MAIN_APP~g" \
            | sed "s~<domain_name>~$DOMAIN_NAME~g" \
            | sed "s~<static_dir>~$STATIC_DIR~g" \
            | sed "s~<media_dir>~$MEDIA_DIR~g" \
            | sed "s~<socket_path>~$SOCKET_PATH~g" \
            | sed "s~<nginx_user>~$NGINX_USER~g" \
            )

    echo "$content" >$PROJECT_DIR/$MAIN_APP/$config

    ((counter++))
done;

sudo python manage.py collectstatic

sudo mkdir -p $NGINX_SERVERS_DIR
sudo ln -sf $PROJECT_DIR/$MAIN_APP/nginx.conf $NGINX_SERVERS_DIR/$MAIN_APP.conf
sudo systemctl start nginx

sudo uwsgi --ini $MAIN_APP/uwsgi.ini --uid=$USER --gid=$USER
sudo rm -f $SOCKET_PATH
