import serial
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyfirmata

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
last = 0
port = '/dev/tty.usbmodem101'
baud_rate = 9600
commandNum = [0, 0, 0, 0, 0]
board = pyfirmata.Arduino(port)
motor1=board.get_pin('m:1:o')
motor2=board.get_pin('m:2:o')
motor3=board.get_pin('m:3:o')
motor4=board.get_pin('m:4:o')

while True:
    arduino = serial.Serial(port, baud_rate)
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup[0] == 1:
                motor1.write(0)
                motor2.write(0)
                motor3.write(0)
                motor4.write(0)
            if fingerup[1] == 1:
                motor1.write(1)
                motor2.write(1)
                motor3.write(1)
                motor4.write(1)
            print(fingerup)
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #arduino.close()
video.release()
cv2.destroyAllWindows()