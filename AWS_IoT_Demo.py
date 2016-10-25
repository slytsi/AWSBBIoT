#  sudu pip install requests
# This is a demo by Kevin Lee
import requests
import time
import grove_temperature_sensor
import grove_oled
import Adafruit_BBIO.GPIO as GPIO
import random
from adxl345 import ADXL345

#dweetIO = "https://dweet.io/dweet/for/"
#myName = "BBG_IoT_Demo"
#myKey = "Temperature"

Buzzer = "P9_22"            # UART2_RXD P9_22
GPIO.setup(Buzzer, GPIO.OUT)
THRESHOLD_TEMPERATURE = 15


if __name__=="__main__":
    
    grove_oled.oled_init()
    grove_oled.oled_setNormalDisplay()
    grove_oled.oled_clearDisplay()
    while True:
        
        #3 Axis
        adxl345 = ADXL345()
        axes = adxl345.getAxes(True)
        xVal = axes['x']
        yVal = axes['y']
        zVal = axes['z']
        #print "x = %.3fG" % ( xVal )
        temperature = grove_temperature_sensor.read_temperature()
        temp_f = temperature * 9.0 / 5.0 + 32.0
        #Placeholders-calculated values
        rpm = random.gauss (5000,50)
        fuellevel= random.gauss (3,.1)
	
        #Screen Controls
        grove_oled.oled_setTextXY(0,0)
        grove_oled.oled_putString("AWS IoT OSMC")
        grove_oled.oled_setTextXY(1,0)
        grove_oled.oled_putString("Engine")
        grove_oled.oled_setTextXY(2,0)
        grove_oled.oled_putString('Temp:{0:0.1f}'.format(temp_f))
        grove_oled.oled_setTextXY(3,0)
        grove_oled.oled_putString('RPM:{0:0.1f} '.format(rpm))
        grove_oled.oled_setTextXY(4,0)
        grove_oled.oled_putString('Fuel:{0:0.1f}'.format(fuellevel))
        grove_oled.oled_setTextXY(5,0)
        grove_oled.oled_putString('Lean X:{0:0.1f}'.format(xVal))
        grove_oled.oled_setTextXY(6,0)
        grove_oled.oled_putString('Lean Y:{0:0.1f}'.format(yVal))
        grove_oled.oled_setTextXY(7,0)
        grove_oled.oled_putString('Lean Z:{0:0.1f}'.format(zVal))
        #Show something to the console
        print 'Temp \n {0:0.2f} *C'.format(temp_f)
        #Check for High Temperature
        if temperature >= THRESHOLD_TEMPERATURE :
            GPIO.output(Buzzer,GPIO.HIGH)
        else:
            GPIO.output(Buzzer,GPIO.LOW)
        time.sleep(1)
