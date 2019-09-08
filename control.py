import socket
from pynput import keyboard

TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024


def on_press(key):
    try:
        print('key {0} pressed'.format(
            key.char))
        if key.char == 'w':
            print('GO')
            s.sendall(b'FORWORD')
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
