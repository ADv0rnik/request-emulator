#!/usr/bin/env bash

cd backend/ && alembic upgrade head

python main.py