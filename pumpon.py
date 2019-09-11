#!/usr/bin/python

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

try:
    
    GPIO.output(2, GPIO.LOW)
    time.sleep(30);
    
    GPIO.cleanup()
    
    print ("Pumping complete")
    
except KeyboardInterrupt:



  print ("Quit")
    
  GPIO.cleanup()
