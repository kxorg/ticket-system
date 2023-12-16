#!/bin/sh
set -e

echo "____________________________________________________________________"
echo "Current user:"
whoami
echo "pwd:"
pwd
echo "____________________________________________________________________"

echo "...Waiting for the database to be ready..."

# Loop until the database port is open
while ! nc -z -w 1 db 5432; do
  echo "sleeping for 1 second..."
  sleep 1
done

echo "...Running Alembic migrations..."
alembic revision --autogenerate -m "message"
echo "alembic select current..."
alembic current
echo "current DONE"
echo "alembic upgrade head..."
alembic upgrade head
echo "upgrade DONE"

echo "...Starting FastAPI app..."
uvicorn main:app --reload --host 0.0.0.0 --port 80
