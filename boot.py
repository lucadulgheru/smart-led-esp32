try:
  import usocket as socket
except:
  import socket

from machine import Pin
from neopixel import NeoPixel
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'UPC65D7E27'
password = 'mtsvecK4fe7a'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

neopixel_strip = NeoPixel(Pin(26), 10)