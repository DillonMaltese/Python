import pyfirmata

port = '/dev/tty.usbmodem101'

board = pyfirmata.Arduino(port)

led_0=board.get_pin('d:3:o')
led_1=board.get_pin('d:5:o')
led_2=board.get_pin('d:6:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')

def led(array):
    if array[0] == 1:
        led_0.write(1)
    else:
        led_0.write(0)
    if array[1] == 1:
        led_1.write(1)
    else:
        led_1.write(0)
    if array[2] == 1:
        led_2.write(1)
    else:
        led_2.write(0)
    if array[3] == 1:
        led_3.write(1)
    else:
        led_3.write(0)
    if array[4] == 1:
        led_4.write(1)
    else:
        led_4.write(0)


