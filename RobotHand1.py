import serial
import cv2
from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino, SERVO, pyfirmata

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
last = 0
port = '/dev/cu.usbmodem101'
baud_rate = 9600
commandNum = [0, 0, 0, 0, 0]
board = Arduino(port)
pinkyPin = 3
ringPin = 5
pointerPin = 6
thumbPin = 10
middlePin = 11
board.digital[pinkyPin].mode=SERVO
board.digital[ringPin].mode=SERVO
board.digital[middlePin].mode=SERVO
board.digital[pointerPin].mode=SERVO
board.digital[thumbPin].mode=SERVO

def upPos(Pin):
    board.digital[Pin].write(0)

def downPos(Pin):
    board.digital[Pin].write(170)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup[0] == 1:
                upPos(thumbPin)
            else:
                downPos(thumbPin)
            if fingerup[1] == 1:
                upPos(pointerPin)
            else:
                downPos(pointerPin)
            if fingerup[2] == 1:
                upPos(middlePin)
            else:
                downPos(middlePin)
            if fingerup[3] == 1:
                upPos(ringPin)
            else:
                downPos(ringPin)
            if fingerup[4] == 1:
                upPos(pinkyPin)
            else:
                downPos(pinkyPin)
            #print(fingerup)
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #arduino.close()
video.release()
cv2.destroyAllWindows()