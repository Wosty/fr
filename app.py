import os
import sys
import json
import time
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  if os.getenv('KEY_WORD').lower() in data['text']:
    faceList = open('faces.txt','r').readlines()
    msg = random.choice(faceList).strip('\n')
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
