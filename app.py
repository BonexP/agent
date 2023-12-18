from flask import Flask, make_response,request
import requests
import base64
app = Flask(__name__)

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
        if key != 'abcabc':
            return "Invalid key"
        item_decoded = base64.b64decode(item_encoded).decode('utf-8')
        response = requests.get(item_decoded)
        
        if response.status_code == 200:
            content = response.text            
            return f"{content}"
        else:
            return make_response("Error: Unable to fetch content from the URL.",504)
    if item_encoded and key:
        return make_response('Both item and key are present in the arguments.',400)
    else:
        return make_response('Either item or key is missing in the arguments.',400)