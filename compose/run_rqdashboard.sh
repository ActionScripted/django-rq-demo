#!/usr/bin/env bash
cd /django-rq

rq-dashboard -p 9181 -u 'redis://redis/0'
