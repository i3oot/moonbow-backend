from moonbowConstants import *
import Image, cStringIO, os

gamma = bytearray(256)
for i in range(256):
	gamma[i] = 0x00 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

def storeImage(id, name):
	handleImg(data)
	writeId(id)

def readId():
	datafile = open(IMGIDFILE, 'r')	
	id = datafile.readline()
	datafile.close()
	return id

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
	app.logger.debug("Sprite is larger than %d in height. Resizing..." % PIXELCOUNT)	
	size = PIXELCOUNT, PIXELCOUNT*img.size[0]/img.size[1]	        
	print size
	img.thumbnail(size, Image.ANTIALIAS)
	
def writeImg(img, datafile):
	pixels = img.load()
	width = img.size[0]
	height = img.size[1]
	for x in range(width):
		for y in range(height):
			value = pixels[x, y]
			r = int(gamma[value[1]])
			g = int(gamma[value[0]])
			b = int(gamma[value[2]])	
			print "--> %d %d %d " % (r, g, b) 
			datafile.write(chr(r))
			datafile.write(chr(g))
			datafile.write(chr(b))

def writeId(id):
	datafile = open(IMGIDFILE, 'w')	
	datafile.write(id)
	datafile.close()
	

