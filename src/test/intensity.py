from pixel import PixelBone_Pixel
import sys

pixels = PixelBone_Pixel(284) 


def set(inte):
	print(inte)
	for led in range(0,pixels.numPixels()):
		pixels.setPixelColor(led, inte, inte, inte);
	pixels.show()
	pixels.moveToNextBuffer()

while(True):
	print("Enter Intensity")
	i=sys.stdin.readline()
	set(int(i))


