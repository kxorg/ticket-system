FROM python:3.11.5-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./backend/logic/requirements.txt /requirements.txt
COPY ./backend/logic/app /app
COPY ./backend/logic/scripts /scripts

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk update && \
    /py/bin/pip install --no-cache-dir -r /requirements.txt --use-pep517 && \
    adduser --disabled-password --gecos '' user && \
    chown -R user:user /app && \ 
    chmod -R 755 /app && \
    chmod -R +x /scripts

WORKDIR /app

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD pg_isready -h localhost -p 5432 || exit 1

RUN ls -l /scripts

ENV PATH="/scripts:/py/bin:$PATH"
USER user
CMD ["run.sh"]
