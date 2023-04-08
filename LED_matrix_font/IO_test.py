from machine import Pin
import utime

p0 = Pin(0, Pin.IN)     # create input pin on GPIO2
p15 = Pin(15, Pin.OUT, drive=Pin.DRIVE_3)    # create output pin on GPIO0

while True:
    print("on")
    p15.on()                 # set pin to "on" (high) level
    utime.sleep_ms(250)
    print("off")
    p15.off()                # set pin to "off" (low) level
    utime.sleep_ms(250)
    print(p0.value())       # get value, 0 or 1

#p6 = Pin(6, Pin.OUT, drive=Pin.DRIVE_3) # set maximum drive strength
