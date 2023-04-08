import utime
import neopixel
from machine import Pin


def clear():
  global np
  global size
  for i in range(size):
    np[i] = (0, 0, 0)
    np.write()


def index(x,y):
    # return 256-index from a x,y coordinates (starting at zero)
    index = 255 - x*16
    if (x % 2 == 0):
        index = index-15+y
    else:
        index = index-y
    print(x,y,index)
    return index


print("=== main.py ===")

#p = machine.Pin.board.X8
p17 = Pin(17, Pin.OUT)
size = 256
np = neopixel.NeoPixel(p17, 256)

clear()

# inf a 3A meme avec m==255
m = 100
#np[index(0,0)] = (m,m,m)
#np[index(0,15)] = (m,0,0)
#np[index(1,0)] = (0,m,0)
#np[index(15,15)] = (0,0,m)
#np[224] = (m,m,m)
# ligne du bas

m = 64
for i in range(16):
    np[index(i,0)] = (16,m,16)
    np[index(i,15)] = (16,m,16)

m = 32
for i in range(9,12):
    for j in range(2,7):
        np[index(i,j)] = (m,m,m)
for i in range(13,16):
    for j in range(2,7):
        np[index(i,j)] = (m,m,m)

for i in range(9,12):
    for j in range(9,14):
        np[index(i,j)] = (m,m,m)
for i in range(13,16):
    for j in range(9,14):
        np[index(i,j)] = (m,m,m)

for i in range(0,3):
    for j in range(2,7):
        np[index(i,j)] = (m,m,m)
for i in range(4,7):
    for j in range(2,7):
        np[index(i,j)] = (m,m,m)

for i in range(0,3):
    for j in range(9,14):
        np[index(i,j)] = (m,m,m)
for i in range(4,7):
    for j in range(9,14):
        np[index(i,j)] = (m,m,m)


#np[0] = (m,m,m)
#np[2] = (m,0,0)
#np[3] = (0,m,0)
#np[4] = (0,0,m)

np.write()
