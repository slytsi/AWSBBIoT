#!/usr/bin/python
# FileName: lcm.py
# Author  : Richard St-Pierre
# Version : 0.0 Nov 6, 2013     Beagle Bone Black version
#
 
import Adafruit_BBIO.GPIO as GPIO
import time
 
# --- Interface Pins ---
CSA_PIN = "P8_14"
SCK_PIN = "P8_16"
SDI_PIN = "P8_18"
 
# --- LCD commands ---
CMD_CLS   = 0x01
CMD_HOME  = 0x02
CMD_ENTRY = 0x06
CMD_SCROL = 0x07
CMD_OFF   = 0x08
CMD_ON    = 0x0C
CMD_CURS  = 0x0E
CMD_LINE1 = 0x80
CMD_LINE2 = 0xC0
CMD_FSET  = 0x30
CMD_FSET2 = 0x38
 
msg       = ['A','B','C']
logo      = 'Logic Supply'
 
 
#--- Initialize pins ---
GPIO.setup(SCK_PIN, GPIO.OUT)
GPIO.setup(SDI_PIN, GPIO.OUT)
GPIO.setup(CSA_PIN, GPIO.OUT)
 
#--- Logo ---
print "BBB SPI LCM test/demo"
 
#--- Send DATA to LCM ---
def lcm_data (data):
  GPIO.output(SCK_PIN, GPIO.LOW)
  for i in range (8):
       if ((data<<i) & 0x80):
          GPIO.output(SDI_PIN, GPIO.HIGH)
       else:
          GPIO.output(SDI_PIN, GPIO.LOW)
       GPIO.output(SCK_PIN, GPIO.HIGH)
       GPIO.output(SCK_PIN, GPIO.LOW)
  GPIO.output(SDI_PIN, GPIO.HIGH)       #data
  GPIO.output(CSA_PIN, GPIO.LOW)        #strobe/en
  GPIO.output(CSA_PIN, GPIO.HIGH)
 
 
 
#--- Send CMD to LCM ---
def lcm_cmd (cmd):
  GPIO.output(SCK_PIN, GPIO.LOW)
  for i in range (8):
        if ((cmd<<i) & 0x80):
           GPIO.output(SDI_PIN, GPIO.HIGH)
        else:
            GPIO.output(SDI_PIN, GPIO.LOW)
        GPIO.output(SCK_PIN, GPIO.HIGH)
        GPIO.output(SCK_PIN, GPIO.LOW)
  GPIO.output(SDI_PIN, GPIO.LOW)        #cmd
  GPIO.output(CSA_PIN, GPIO.LOW)        #strobe/en
  GPIO.output(CSA_PIN, GPIO.HIGH)
 
 
def lcm_msg (msg):
    for char in msg:
       lcm_data(ord(char))
 
 
def lcm_init ():
    lcm_cmd(CMD_FSET)
    lcm_cmd(CMD_FSET)
    lcm_cmd(CMD_ENTRY)
    lcm_cmd(CMD_ON)
    lcm_cmd(CMD_CLS)
 
 
#--- Init and Display ---
 
lcm_init()
time.sleep(0.1)
 
while True:
  lcm_cmd(CMD_CLS)
  lcm_data(0x42)
  lcm_data(0x45)
  lcm_data(0x41)
  lcm_data(0x47)
  lcm_data(0x4C)
  lcm_data(0x45)
  lcm_data(0x20)
  lcm_data(0x42)
  time.sleep(2)
  lcm_cmd(CMD_CLS)
  time.sleep(0.1)
  lcm_cmd(CMD_CLS)
  lcm_msg("Logic")
  time.sleep(2)
  lcm_cmd(CMD_CLS)
  lcm_msg("Supply")
  time.sleep(2)

