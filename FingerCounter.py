import serial
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
last = 0;
#port = '/dev/tty.usbmodem101'
#baud_rate = 9600
#arduino = serial.Serial(port, baud_rate)
#commandOn = '10on'
#commandOff = '10off'

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                if last != 1:
                    last = 1
                    print(last)
                    #arduino.write(commandOn.encode())

            if fingerup == [0, 1, 1, 0, 0]:
                if last != 2:
                    last = 2
                    print(last)

            if fingerup == [0, 1, 1, 1, 0]:
                if last != 3:
                    last = 3
                    print(last)

            if fingerup == [0, 1, 1, 1, 1]:
                if last != 4:
                    last = 4
                    print(last)

            if fingerup == [1, 1, 1, 1, 1]:
                if last != 5:
                    last = 5
                    print(last)
            if fingerup == [0, 0, 0, 0, 0]:
                if last != 0:
                    last = 0
                    print(last)
                    #arduino.write(commandOff.encode())

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()