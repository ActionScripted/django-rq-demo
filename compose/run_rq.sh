#!/usr/bin/env bash
cd /django-rq

python manage.py rqworker default
