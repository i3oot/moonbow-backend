import Image, cStringIO, os, settings

#gamma = bytearray(256)
#for i in range(256):
#	gamma[i] = 0x00 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

def storeImage(id, data):
	handleImg(data)
	writeId(id)

def readId():
	datafile = open(settings.IMGIDFILE, 'r')	
	id = datafile.readline()
	datafile.close()
	return id

def handleImg(data):
	img = Image.open(cStringIO.StringIO(data)).convert("RGB")
	pixels = img.load()
	width = img.size[0]
	height = img.size[1]
	#app.logger.info("Got Sprite. Dimension: %dx%d pixels" % img.size)
	
	if(height > settings.PIXELCOUNT):
		resize(img)

	#app.logger.debug("Writing converted bytes")
	datafile = open(settings.PIXELBUFFER, 'wb')	
	writeImg(img, datafile)
	datafile.close()
	
def resize (img):
	#app.logger.debug("Sprite is larger than %d in height. Resizing..." % PIXELCOUNT)	
	size = settings.PIXELCOUNT, settings.PIXELCOUNT*img.size[0]/img.size[1]	        
	print size
	img.thumbnail(size, Image.ANTIALIAS)
	
def writeImg(img, datafile):
	pixels = img.convert('RGB')
	width = img.size[0]
	height = img.size[1]
	for x in range(width):
		for y in range(height):
			r,g,b = pixels[x, y]
			#print "--> %d %d %d " % (r, g, b) 
			datafile.write(chr(r))
			datafile.write(chr(g))
			datafile.write(chr(b))

def writeId(id):
	datafile = open(settings.IMGIDFILE, 'w')	
	datafile.write(id)
	datafile.close()
	

