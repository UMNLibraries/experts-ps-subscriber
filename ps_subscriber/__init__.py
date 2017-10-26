import xmltodict

import logging
from logging.handlers import RotatingFileHandler

import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

from flask import Flask, request, jsonify
app = Flask(__name__)

handler = RotatingFileHandler(
  os.getenv('PS_SUBSCRIBER_LOG_FILE'),
  maxBytes=10000,
  backupCount=1
)
handler.setLevel(logging.INFO)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route('/', methods=['POST'])
def person():
  app.logger.info('testing...')
  app.logger.info(request.data.decode('utf-8'))
  response = jsonify(xmltodict.parse(request.data))
  response.status_code = 201
  return response
