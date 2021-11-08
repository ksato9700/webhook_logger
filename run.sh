#!/bin/sh
uvicorn webhook_logger.main:app --host 0.0.0.0 --port 8080


