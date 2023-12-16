#!/bin/sh
set -e

whoami
pwd

echo "...Waiting for the database to be ready..."

# Loop until the database port is open
while ! nc -z -w 1 db 5432; do
  sleep 1
done

echo "...Running Alembic migrations..."
alembic current
alembic upgrade head

echo "...Starting FastAPI app..."
uvicorn main:app --reload --host 0.0.0.0 --port 80
