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
    print(json.dumps(request.get_json(), indent=2))
    return ''
