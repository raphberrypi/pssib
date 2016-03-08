#!/usr/bin/python

# program glowny
# TODO:
# 1. Sterowanie / menu
# 2. DHT22
# 3. RFID
 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print("Importowanie modulu LCD") # print kontrolny
import LCDmazi
print("Importowanie modulu adc") # print kontrolny
import adc

# MAIN
if __name__ == '__main__':
    
    wyswietlacz = LCDmazi.LCD() # tworzenie nowego obiektu klasy LCD

    # czyszczenie i pisanie dla sprawdzenia poprawnosci dzialania
    wyswietlacz.clear()
    wyswietlacz.msg("LCD CHECK...")
    sleep(3)
    wyswietlacz.clear()
    wyswietlacz.msg("PASS")
    sleep(1)
    wyswietlacz.clear()

    # 10 testowych odczytow z przetwornika do ktorego podpiety jest fotorezystor
    # todo: +potencjometr (fotorezystor tryb auto / potek tryb manualny)
    # maybe todo: analogowy czujnik temperatury TMP36
    for i in range (1,11):
        read = adc.analog_read(0) # kanał 0 przetwornika ADC
        volt = read * 3.3 / 1024
        print("Odczyt=%d\tU=%f" % (read, volt)) # kontrolny print
        wyswietlacz.clear() 
        wyswietlacz.msg(str(read))
        # wartosc powyzej nie bedzie wyswietlana
        # stad brak troski o formatowanie
        sleep(1)
        

wyswietlacz.clear()
GPIO.cleanup()
        


