from adafruit_circuitplayground.express import cpx
import time

BLUE = (0, 0, 255)

i = 0

while True:
    # start your code here
    if i == 10:
        time.sleep(10)
        continue
    cpx.pixels[i] = BLUE
    i += 1
    time.sleep(0.5)
