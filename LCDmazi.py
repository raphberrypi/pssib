#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

class LCD:

    def __init__(self, PIN_RS=25, PIN_E=24, PINS_DB=[23,17,21,22]):
        
        print("Zaimportowano modul LCD-mazi")
        self.PIN_RS = PIN_RS # RS linia komend
        self.PIN_E = PIN_E # starts data read/write
        self.PINS_DB = PINS_DB # linie danych
        
        GPIO.setup(self.PIN_E, GPIO.OUT) # E wyjscie
        GPIO.setup(self.PIN_RS, GPIO.OUT) # RS wyjscie
        for PIN in self.PINS_DB: # dane wyjscia
            GPIO.setup(PIN, GPIO.OUT)
        # Initialize LCD (Datasheet)
        self.cmd(0b00110011)
        self.cmd(0b00110010)
        self.cmd(0b00101000) #function set D=0, N=1, F=0
        self.cmd(0b00001101) #Display Off D=0, C=0, B=1
        self.cmd(0b00000001)
        self.cmd(0b00000110)
  
    def clear(self):
        """ Reset LCD """

        self.cmd(0b00000010)
        self.cmd(0b00000001)
        self.cmd(0b00000010)
        
    def cmd(self, command, TRUE_FALSE=False):
        """ Komenda do wyswietlacza """

        sleep(0.001)
        command=bin(command)[2:].zfill(8)
        GPIO.output(self.PIN_RS, TRUE_FALSE) # RS = 0, linia komend
        #print("Komenda: ", command) 

        for PIN in self.PINS_DB:
            GPIO.output(PIN, False)

        for i in range(4):
            if command[i] == "1":
                GPIO.output(self.PINS_DB[::-1][i], True)
                #print(self.PINS_DB[::-1][i]) # print do debugowania

        GPIO.output(self.PIN_E, True)
        sleep(0.001)
        GPIO.output(self.PIN_E, False)

        for PIN in self.PINS_DB:
            GPIO.output(PIN, False)

        for i in range(4,8):
            if command[i] == "1":
                GPIO.output(self.PINS_DB[::-1][i-4], True)
                #print(self.PINS_DB[::-1][i-4]) # print do debugowania

        GPIO.output(self.PIN_E, True)
        sleep(0.001)
        GPIO.output(self.PIN_E, False)

    
    def msg(self, text):
        """ msg """

        for char in text:
            if char == '\n':
                self.cmd(0xC0) 
            else:
                self.cmd(ord(char),True)



    
    

