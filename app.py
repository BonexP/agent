from flask import Flask, make_response,request
import requests
import base64
import yaml
import os
from dotenv import load_dotenv

app = Flask(__name__)

def load_yaml(path):
    with open(path) as f:
        d=yaml.load(f, Loader=yaml.FullLoader)
        for i in d:
            app.config[i]=d[i]
        return d
    

load_yaml('config.yaml')
load_dotenv('.env')

print(f"key from config.yaml is {app.config['key']}")
print(f"key from .env is {os.getenv('KEY')}")

if os.getenv('KEY')==None:
    pass
elif os.getenv('KEY'):
    app.config.update(key=os.getenv('KEY'))

print(f"final key is {app.config['key']}")


def proxy(url):
    r = requests.get(url)
    if r.status_code == 200:          
        return r.content
    else:
        return make_response("Error: Unable to fetch content from the URL.",504)

        


@app.route('/pre')
def pre():
    id=request.args.get('id')
    return proxy(app.config['items'][id])
    

@app.route('/')
def hello_world():
    return make_response("",200)
    # return 200
    # return 'Hello, World!'


@app.route('/check_args', methods=['GET'])
def check_args():
    item_encoded = request.args.get('item')
    key = request.args.get('key')

    if item_encoded and key:
        if key != app.config['key']:
            return "Invalid key"
        item_decoded = base64.b64decode(item_encoded).decode('utf-8')
        return proxy(item_decoded)
    if item_encoded and key:
        return make_response('Both item and key are present in the arguments.',400)
    else:
        return make_response('Either item or key is missing in the arguments.',400)