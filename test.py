#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.output(5, GPIO.HIGH)
time.sleep(5)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.HIGH)
time.sleep(5)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
time.sleep(5)
GPIO.output(13, GPIO.LOW)
