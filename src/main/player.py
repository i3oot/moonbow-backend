from pixel import PixelBone_Pixel
from time import sleep
import struct, settings

pixels = PixelBone_Pixel(settings.PIXELCOUNT) 

def play():
	datafile = open(settings.PIXELBUFFER, 'rb')	
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
			sleep(settings.framesleep())
	except Exception as e:
		print("EOF")
	finally:
		datafile.close()
		clear()

def pulse():
	for i in range(0, 2*3.14, 0.05):
		intensity = int(sin(i) * 255);
		for led in range(0,pixels.numPixels()):
			pixels.setPixelColor(led, intensity, intensity, intensity);
			sleep(0.05)
	clear()

def clear():
	for led in range(0,pixels.numPixels()):
		pixels.setPixelColor(led, 0, 0, 0)
		pixels.show()
		pixels.moveToNextBuffer()


