from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)


# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle',
                       use_unicode=True, charset='utf8')


# IP address of NodeMCU
address = 'http://192.168.0.6'

response_dict = {"response": {
"outputSpeech": {
"text": "",
"type": "PlainText"
},
"shouldEndSession": True
},
"sessionAttributes": {},
"version": "1.0"
}


@app.route('/', methods=['POST'])
def index():
    print(type(request.data))
    print(type(request.json))

    request_json = request.json
    intent = get_intent_from_request(request_json)

    result = ''
    if intent == 'HELLO_INTENT':
        result = handle_hello_intent()
    elif intent == 'BYE_INTENT':
        result = handle_bye_intent()
    else:
        result = handle_fallback_intent()

    response_dict['response']['outputSpeech']['text'] = result

    return jsonify(json.dumps(response_dict))


def get_intent_from_request(request_json):
    intent = request_json['request']['intent']['name']
    return intent


def handle_hello_intent():
    return "Hi my name is HR. Nice to meet you"


def handle_bye_intent():
    return "Bye bye~"


def handle_fallback_intent():
    return "I'm sorry, I can not understand."


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)