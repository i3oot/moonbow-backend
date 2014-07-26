import sys
sys.path.append("../main")
from moonbowPlayer import play
from moonbowServer import writeImg
from moonbowConstants import PIXELBUFFER

img = Image.open('basictest8x8.png').convert("RGB")
buf = open(FIXELBUFFER, "wb")
writeImg(img, buf)
buf.close() 
play()

