import json
import logging
from datetime import datetime as dt
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    timestamp = dt.now().strftime("%d/%b/%Y %I:%M:%S")
    app.logger.info(f'[{timestamp}] Received a notification')
    if request.mimetype == "application/json":
        print(json.dumps(request.json, indent=2))
        return ''
    # elif request.mimetype == 'application/x-www-form-urlencoded':
    #   print(request.form)
    #   return ''
    else:
        app.logger.error(f"Unknown content-type: {request.mimetype}")
        return '', 400
