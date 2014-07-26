from pixel import PixelBone_Pixel
from moonbowConstants import PIXELBUFFER
from moonbowConstants import PIXELCOUNT
from moonbowConstants import FRAMESLEEP
from time import sleep
import struct

def play():
	pixels = PixelBone_Pixel(PIXELCOUNT) 
	datafile = open(PIXELBUFFER, 'rb')	
	try:
		while(True): #breaks at eof.
			for led in range(0,pixels.numPixels()):
				r = struct.unpack('B', datafile.read(1))[0]
				g = struct.unpack('B', datafile.read(1))[0]
				b = struct.unpack('B', datafile.read(1))[0]
			
				#print "%d,%d,%d" % (r,g,b)
				pixels.setPixelColor(led, r,g,b)
			pixels.show()
			pixels.moveToNextBuffer()
			sleep(FRAMESLEEP)
	finally:
		datafile.close()


