import socket
from pynput import keyboard
import threading

TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024

counter = 0


def on_press(key):
    try:
        global counter
        print('key {0} pressed'.format(
            key.char))
        if key.char == 'w':
            print('GO')
            s.sendall(b'FORWORD')
            counter = counter+1
            if counter == 4:
                print("Incress speed to: 50")
                s.sendall(b'MED_SPEED')
            elif counter == 8:
                print("Incress speed to: 75")
                s.sendall(b'HIGH_SPEED')
            elif counter == 16:
                print("Incress speed to: 100")
                s.sendall(b'MAX_SPEED')
        elif key.char == 's':
            print('BACK')
            s.sendall(b'BACK')
        elif key.char == 'a':
            print('LEFT')
            s.sendall(b'LEFT')
        elif key.char == 'd':
            print('RIGHT')
            s.sendall(b'RIGHT')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    global counter
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        s.sendall(b'STOP')
        res = s.recv(16)
        print(res)
        s.close()
        return False
    elif key.char == 'w':
        s.sendall(b'FORWORD_STOP')
        counter = 0
        s.sendall(b'LOW_SPEED')
    elif key.char == 's':
        s.sendall(b'BACK_STOP')
    elif key.char == 'a':
        s.sendall(b'LEFT_STOP')
    elif key.char == 'd':
        s.sendall(b'RIGHT_STOP')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
