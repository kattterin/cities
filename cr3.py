import json

from flask import Flask, jsonify
# import logging
app = Flask(__name__)

# logging.basicConfig(level=logging.INFO)

@app.route('/')
def main():
    # logging.info(f'Request: {request.json!r}')
    with open('data.json') as f:
        return jsonify(json.load(f))

    # data = json.load(open('data.json'))
    # return jsonify(data)


if __name__ == '__main__':
    app.run()