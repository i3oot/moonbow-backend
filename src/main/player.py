from pixel import PixelBone_Pixel
from time import sleep
import struct, settings, numpy, math

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
	for i in numpy.arange(0, 2*math.pi, 0.05):
		intensity = int(math.pow(math.fabs(math.sin(i)), 2.5) * 60);
		for led in range(0,pixels.numPixels()):
			pixels.setPixelColor(led, intensity, intensity, intensity);
		pixels.show()
		pixels.moveToNextBuffer()
		sleep(0.01)

def clear():
	pixels.moveToNextBuffer()
	for led in range(0,pixels.numPixels()):
		pixels.setPixelColor(led, 0, 0, 0)
	pixels.show()
	pixels.moveToNextBuffer()


