import sys
import Image
sys.path.append("../main")
from moonbowPlayer import play
from moonbowServer import writeImg
from moonbowConstants import PIXELBUFFER

img = Image.open('basictest8x8.png').convert("RGB")
buf = open(PIXELBUFFER, "wb")
writeImg(img, buf)
buf.close() 
play()

