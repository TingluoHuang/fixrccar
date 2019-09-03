#!/usr/bin/python

import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(23, gpio.OUT)

def forward():
    init()
    gpio.output(17, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    time.sleep(0.2)
    gpio.cleanup()

def back():
    init()
    gpio.output(17, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    time.sleep(0.2)
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

    # if (char == "a"):
    #     print 'Left pressed'
    #     Left()
    #     time.sleep(button_delay)

    # if (char == "d"):
    #     print 'Right pressed'
    #     Right()
    #     time.sleep(button_delay)          

    elif (char == "w"):
        print 'Up pressed' 
        forward()       
    
    elif (char == "s"):
        print 'Down pressed'      
        back()