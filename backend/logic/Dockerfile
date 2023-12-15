FROM python:3.11.5-alpine3.18

COPY ./backend/logic/requirements.txt /requirements.txt
COPY ./backend/logic /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
WORKDIR /app/app

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD pg_isready -h localhost -p 5432 || exit 1

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]