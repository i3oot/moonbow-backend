from flask import Flask, json, request
from flask.ext.cors import cross_origin
from base64 import b64decode
from sprite import storeImage, readId

app = Flask(__name__)

@app.route('/sprite', methods=['POST'])
@cross_origin(headers=['Content-Type'])
def spritePost():
	msg = request.json
	app.logger.debug("Request: " + json.dumps(msg))
	img = b64decode(msg['data'])
	storeImage(msg['id'], img)
	return "ok"

@app.route('/sprite', methods=['GET', 'OPTIONS'])
@cross_origin(headers=['Content-Type'])
def spriteGet():
   return readId()

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')


