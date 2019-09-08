#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import socket

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)

def forward():
    # gpio.output(22, gpio.LOW)
    # gpio.output(23, gpio.LOW)
    gpio.output(17, gpio.HIGH)
    gpio.output(18, gpio.LOW)

def forward_stop():
    # gpio.output(22, gpio.LOW)
    # gpio.output(23, gpio.LOW)
    gpio.output(17, gpio.LOW)
    gpio.output(18, gpio.LOW)


def back():
    # gpio.output(22, gpio.LOW)
    # gpio.output(23, gpio.LOW)
    gpio.output(17, gpio.LOW)
    gpio.output(18, gpio.HIGH)

def back_stop():
    # gpio.output(22, gpio.LOW)
    # gpio.output(23, gpio.LOW)
    gpio.output(17, gpio.LOW)
    gpio.output(18, gpio.LOW)

def left():
    # gpio.output(17, gpio.LOW)
    # gpio.output(18, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)

def left_stop():
    # gpio.output(17, gpio.LOW)
    # gpio.output(18, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)

def right():
    # gpio.output(17, gpio.LOW)
    # gpio.output(18, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)

def right_stop():
    # gpio.output(17, gpio.LOW)
    # gpio.output(18, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)

def stop():
    gpio.output(17, gpio.LOW)
    gpio.output(18, gpio.LOW)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.LOW)
    gpio.cleanup()

print(gpio.VERSION)

init()

TCP_PORT = 9999
BUFFER_SIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print(addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        break

    data = data.decode()
    print(data)
    if data == 'FORWORD':
        forward()
    elif data == 'FORWORD_STOP':
        forward_stop()
    elif data == 'BACK':
        back()
    elif data == 'BACK_STOP':
        back_stop()
    elif data == 'LEFT':
        left()
    elif data == 'LEFT_STOP':
        left_stop()
    elif data == 'RIGHT':
        right()
    elif data == 'RIGHT_STOP':
        right_stop()      
    elif data == 'STOP':
        conn.sendall(b'ACK')
        break

conn.close()
stop()

# # import sys, termios, tty, os

# # def getch():
# #     fd = sys.stdin.fileno()
# #     old_settings = termios.tcgetattr(fd)
# #     try:
# #         tty.setraw(sys.stdin.fileno())
# #         ch = sys.stdin.read(1)

# #     finally:
# #         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
# #     return ch

# init()

# def on_press(key):
#     print('{0} pressed'.format(
#         key))
#     if (char == "a"):
#         left()

#     elif (char == "d"):
#         right()

#     elif (char == "w"): 
#         forward()       
    
#     elif (char == "s"):      
#         back()

# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         stop()
#         return False
    
#     elif (char == "a"):
#         left_stop()

#     elif (char == "d"):
#         right_stop()

#     elif (char == "w"):
#         forward_stop()

#     elif (char == "s"):
#         back_stop()

# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     os.environ['DISPLAY'] = os.environ['REMOTE_DISPLAY']
#     listener.join()


# # while True:
# #     char = getch()

# #     if (char == "q"):
# #         stop()
# #         exit(0)  

# #     if (char == "a"):
# #         print 'Left pressed'
# #         left()
# #     #     time.sleep(button_delay)

# #     if (char == "d"):
# #         print 'Right pressed'
# #         right()
# #     #     time.sleep(button_delay)          

# #     elif (char == "w"):
# #         print 'Up pressed' 
# #         forward()       
    
# #     elif (char == "s"):
# #         print 'Down pressed'      
# #         back()