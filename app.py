from flask import Flask,request
import requests
import base64
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


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
            return "Error: Unable to fetch content from the URL."  
    if item_encoded and key:
        return 'Both item and key are present in the arguments.'
    else:
        return 'Either item or key is missing in the arguments.'