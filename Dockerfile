FROM python:3.10 as builder
WORKDIR /usr/src/app
COPY webhook_logger webhook_logger
COPY pyproject.toml pyproject.toml
RUN pip install --upgrade pip \
  && pip install .

FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Tokyo
WORKDIR /usr/src/app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
EXPOSE $PORT
CMD uvicorn webhook_logger.main:app --host 0.0.0.0 --port $PORT
