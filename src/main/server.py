from flask import Flask, json, request
from flask.ext.cors import cross_origin
from base64 import b64decode
import sprite, settings, player

app = Flask(__name__)

@app.route('/sprite', methods=['POST'])
@cross_origin(headers=['Content-Type'])
def spritePost():
	msg = request.json
	app.logger.debug("Request: " + json.dumps(msg))
	img = b64decode(msg['data'])
	sprite.storeImage(msg['id'], img)
	return sprite.readId()

@app.route('/sprite', methods=['GET', 'OPTIONS'])
@cross_origin(headers=['Content-Type'])
def spriteGet():
   return sprite.readId()

@app.route('/settings/framesleep', methods=['POST'])
@cross_origin(headers=['Content-Type'])
def framesleepPost():
	msg = request.json
	app.logger.debug("Request: " + json.dumps(msg))
	newvalue = msg['framesleep']
	app.logger.debug("New Framesleep value: " + newvalue)
	return settings.framesleep(newvalue)

@app.route('/settings/framesleep', methods=['GET', 'OPTIONS'])
@cross_origin(headers=['Content-Type'])
def framesleepGet():
	return settings.framesleep()



if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host='0.0.0.0')
    player.pulse()

