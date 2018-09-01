import os
import sys
import json
import time

#from groupy.client import Client
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  if '?' in data['text']:
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    time.sleep(2)
    msg = 'Read the syllabus.'
    send_message(msg)
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
