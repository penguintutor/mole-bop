# Uses mcp23008 from https://github.com/CrankshawNZ/Micropython
from machine import Pin, I2C
import mcp23008
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

print('Scan i2c bus...')
devices = i2c.scan()
print (devices)

mcp = mcp23008.MCP23008(i2c, 0x20)

mcp.setPinDir(0,1)
mcp.setPinDir(1,1)
mcp.setPullupOn(0)
mcp.setPullupOn(1)



while True:
    print ("buttons  {} :  {} ".format(mcp.readPin(0), mcp.readPin(1)))
    time.sleep(1)    