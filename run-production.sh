#!/bin/bash

PROJECT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
STATIC_DIR="/srv/http/static"

cat $PROJECT_DIR/medici_server/nginx_template.conf | sed "s~<project_dir>~$PROJECT_DIR~g" \
>$PROJECT_DIR/medici_server/nginx.conf

cat $PROJECT_DIR/medici_server/uwsgi_template.ini | sed "s~<project_dir>~$PROJECT_DIR~g" \
>$PROJECT_DIR/medici_server/uwsgi.ini

cat $PROJECT_DIR/medici_server/settings_template.py | sed "s~<static_dir>~'$STATIC_DIR'~g" \
>$PROJECT_DIR/medici_server/settings.py

sudo python manage.py collectstatic

sudo systemctl start nginx
uwsgi --ini medici_server/uwsgi.ini
