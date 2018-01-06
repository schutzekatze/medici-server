#!/bin/bash

./config.sh
source config.sh

DJANGO_DEBUG=True ./manage.py runserver
