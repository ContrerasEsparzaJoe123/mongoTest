#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://joec:that1guy2@cluster0-tlgse.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["parcial2"]
collection = db["posts"]

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print
    "Waiting for sensor to settle"

    time.sleep(2)

    print
    "Calculating distance"

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print
    "Distance:", distance, "cm"

    post = {"Distanncia": str(distance)}

    collection.insert_one(post)
finally:
    GPIO.cleanup()
    time.sleep(2)


