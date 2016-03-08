#!/usr/bin/python
# Obsluga MCP3008

import spidev
import RPi.GPIO as GPIO
from time import sleep

spi = spidev.SpiDev()
spi.open(0,0)

def analog_read(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    print(adc)
    adc_out = ((adc[1]&3) << 8) + adc[2]
    return adc_out



    
        


