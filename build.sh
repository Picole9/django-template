#!/bin/bash
if [[ $(docker compose ps | grep web) ]]; then
    docker compose cp web:/django/db.sqlite3 .
    docker compose down
fi
docker compose build
docker compose up -d --remove-orphans
