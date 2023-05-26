#!/usr/bin/env bash

cd backend/ && alembic upgrade head

LOAD_FIXTURE=False

if [ "$LOAD_FIXTURE" = True ]
then
  echo "Run init database"
  python run_db.py
fi

python main.py