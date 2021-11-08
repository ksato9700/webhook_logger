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
    jsondata = await request.json()
    if content_type == "application/json":
        logger.info(json.dumps(jsondata, indent=2))
        return ""
    else:
        raise HTTPException(
            status_code=400, detail=f"Unknown content-type: {content_type}"
        )
