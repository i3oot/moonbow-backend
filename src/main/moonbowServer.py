from flask import Flask
from flask import json
from flask import request
from base64 import b64decode
from moonbowConstants import PIXELBUFFER
from moonbowConstants import PIXELCOUNT
import Image, cStringIO, os

app = Flask(__name__)

gamma = bytearray(256)
for i in range(256):
	gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)


def handleImg(data):
	img = Image.open(cStringIO.StringIO(data)).convert("RGB")
	pixels = img.load()
	width = img.size[0]
	height = img.size[1]
	app.logger.info("Got Sprite. Dimension: %dx%d pixels" % img.size)
	
	if(height > PIXELCOUNT):
		resize(img)

	app.logger.debug("Writing converted bytes")
	datafile = open(PIXELBUFFER, 'wb')	
	writeImg(img, datafile)
	datafile.close()
	
def resize (img):
	app.logger.debug("Sprite is larger than %d in height. Resizing..." % maxheight)	
	size = maxheight, (PIXELCOUNT/height)*width	        
	img.thumbnail(size, Image.ANTIALIAS)
	
def writeImg(img, datafile):
	width = img.size[0]
	height = img.size[1]
	for x in range(width):
		for y in range(height):
			value = pixels[x, y]
			datafile.write(bytes(gamma[value[1]]))
			datafile.write(bytes(gamma[value[0]]))
			datafile.write(bytes(gamma[value[2]]))


@app.route('/sprite', methods=['POST'])
def sprite():
	msg = request.json
	app.logger.debug("Request: " + json.dumps(msg))
	img = b64decode(msg['data'])
	handleImg(img)
	return "ok"   

if __name__ == '__main__':
    app.run(debug=True)


