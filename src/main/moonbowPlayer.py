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
				color = int(datafile.read(3))
				pixels.setPixelColor(led, color)
			pixels.show()
			pixels.moveToNextBuffer()
			sleep(FRAMESLEEP)
	finally:
		datafile.close()


