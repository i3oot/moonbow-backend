from pixel import PixelBone_Pixel
from moonbowConstants import PIXELBUFFER
from moonbowConstants import PIXELCOUNT
from moonbowConstants import FRAMESLEEP
from time import sleep

def play():
	pixels = PixelBone_Pixel(PIXELCOUNT) 
	datafile = open(PIXELBUFFER, 'rb')	
	try:
		while(True): #breaks at eof.
			for led in range(0,pixels.numPixels()):
				r = datafile.read(1)
				g = datafile.read(1)
				b = datafile.read(1)	    
				pixels.setPixelColor(led, r, g, b)
			pixels.show()
			pixelsmoveToNextBuffer()
			sleep(FRAMESLEEP)
	finally:
		datafile.close()


