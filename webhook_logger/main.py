import logging
import json
from datetime import datetime as dt
from fastapi import FastAPI, Request, HTTPException, Header

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/", status_code=200)
async def post(request: Request, content_type=Header(None)):
    timestamp = dt.now().strftime("%d/%b/%Y %H:%M:%S")
    logger.info(f"[{timestamp}] Received a notification")
    if content_type == "application/json":
        jsondata = await request.json()
        logger.info(json.dumps(jsondata, indent=2))
        return ""
    else:
        body = await request.body()
        logger.info(f"Content-Type: {content_type}")
        logger.info(f"Body: {repr(body)}")
