FROM python:3.10-slim-buster
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Tokyo

COPY webhook_logger webhook_logger
COPY pyproject.toml pyproject.toml
RUN pip install --upgrade pip \
  && pip install .
EXPOSE $PORT
CMD uvicorn webhook_logger.main:app --host 0.0.0.0 --port $PORT
