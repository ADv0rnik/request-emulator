#!/usr/bin/env bash

cd backend/ && alembic upgrade head

LOAD_FIXTURE=True

if [ "$LOAD_FIXTURE" = True ]
then
  echo "Run init database"
  python initial_db.py
fi

python main.py