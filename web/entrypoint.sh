#!/bin/sh

uwsgi --ini app.ini

exec "$@"