#  sudu pip install requests
# This is a demo by Kevin Lee
import requests
import time
import grove_temperature_sensor
import grove_oled
import Adafruit_BBIO.GPIO as GPIO
import random

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
        # GPIO.output(led,GPIO.HIGH)
        # time.sleep(1)
        # GPIO.output(led,GPIO.LOW)
        # time.sleep(1)
        # print 'led'
        temperature = grove_temperature_sensor.read_temperature()
        temp_f = temperature * 9.0 / 5.0 + 32.0
        rpm = random.gauss (5000,50)
        fuellevel= random.gauss (3,.1)
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
        grove_oled.oled_setTextXY(6,0)
        grove_oled.oled_putString("AWS IoT")

        print 'Temp \n {0:0.2f} *C'.format(temp_f)

        #rqsString = dweetIO + myName + '?' + myKey + '=' + '{0:0.1f} '.format(temperature)
        # +'/' +  myKey + '=' + '{0:0.1f} *C'.format(sensor.read_temperature())
        # rqsString = dweetIO + myName + '?' + "{'Temperatuer':'23C','ADC':'123'}"
        #print rqsString
        #rqs = requests.get(rqsString)
        #print rqs.status_code
        #print rqs.headers
        #print rqs.content
        if temperature >= THRESHOLD_TEMPERATURE :
            GPIO.output(Buzzer,GPIO.HIGH)
        else:
            GPIO.output(Buzzer,GPIO.LOW)
        time.sleep(1)
