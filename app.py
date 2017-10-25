import xmltodict
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
PSSubscriber = Flask(__name__)

@PSSubscriber.route('/ps_subscriber/', methods=['POST'])
def person():
  PSSubscriber.logger.info('testing...')
  PSSubscriber.logger.info(request.data.decode('utf-8'))
  response = jsonify(xmltodict.parse(request.data))
  response.status_code = 201
  return response

if __name__ == '__main__':
  handler = RotatingFileHandler('ps_subscriber.log', maxBytes=10000, backupCount=1)
  handler.setLevel(logging.INFO)
  PSSubscriber.logger.setLevel(logging.INFO)
  PSSubscriber.logger.addHandler(handler)
  PSSubscriber.run()
