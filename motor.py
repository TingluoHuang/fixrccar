#!/usr/bin/python

import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)

def forward():
    init()
    gpio.output(17, gpio.HIGH)
    gpio.output(18, gpio.LOW)
    gpio.cleanup()

def back():
    init()
    gpio.output(17, gpio.LOW)
    gpio.output(18, gpio.HIGH)
    gpio.cleanup()

def left():
    init()
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    gpio.cleanup()

def right():
    init()
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    gpio.cleanup()

print(gpio.VERSION)

import sys, termios, tty, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    char = getch()

    if (char == "q"):
        exit(0)  

    if (char == "a"):
        print 'Left pressed'
        left()
    #     time.sleep(button_delay)

    if (char == "d"):
        print 'Right pressed'
        right()
    #     time.sleep(button_delay)          

    elif (char == "w"):
        print 'Up pressed' 
        forward()       
    
    elif (char == "s"):
        print 'Down pressed'      
        back()