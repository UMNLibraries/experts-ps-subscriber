import xmltodict
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
PSSubscriber = Flask(__name__)

@app.route('/persons/', methods=['POST'])
def person():
  app.logger.info('testing...')
  app.logger.info(request.data.decode('utf-8'))
  response = jsonify(xmltodict.parse(request.data))
  response.status_code = 201
  return response

if __name__ == '__main__':
  handler = RotatingFileHandler('persons.log', maxBytes=10000, backupCount=1)
  handler.setLevel(logging.INFO)
  app.logger.setLevel(logging.INFO)
  app.logger.addHandler(handler)
  app.run()
