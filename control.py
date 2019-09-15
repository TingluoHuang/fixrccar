import socket
from pynput import keyboard
import threading 

TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024

def speedUp(target):
    print("Incress speed to: " + target)
    if target == 50:
        speedTimer_2.start()
    elif target == 75:
        speedTimer_3.start()

speedTimer_1 = threading.Timer(0.25, speedUp(50))
speedTimer_2 = threading.Timer(0.25, speedUp(75))
speedTimer_3 = threading.Timer(0.25, speedUp(100))

def on_press(key):
    try:
        print('key {0} pressed'.format(
            key.char))
        if key.char == 'w':
            print('GO')
            s.sendall(b'FORWORD')
            speedTimer_1.start()
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
        speedTimer_1.cancel()
        speedTimer_2.cancel()
        speedTimer_3.cancel()
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
