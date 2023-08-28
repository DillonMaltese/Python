import cv2
import mediapipe as mp
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
detector = HandDetector(maxHands=1, detectionCon=0.8)
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    _, img = webcam.read()
    hand = detector.findHands(img, draw=True)
    #applying hand tracking
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mp_hands.Hands().process(img)
    if results.multi_hand_landmarks:
        for i in results.multi_handedness:

            # Return whether it is Right or Left Hand
            label = MessageToDict(i)[
                'classification'][0]['label']

            if label == 'Right':
                # Display 'Left Hand' on left side of window
                cv2.putText(img, label + ' Hand', (20, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 0.9,
                            (0, 255, 0), 2)

            if label == 'Left':
                # Display 'Left Hand' on left side of window
                cv2.putText(img, label + ' Hand', (460, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.9, (0, 255, 0), 2)

    #results = mp_hands.process(img)
    # lmlist = []
    # if detector.results.multi_hand_landmarks:
    #     myHand = detector.results.multi_hand_landmarks[0]
    # #     for id, lm in enumerate(myHand.landmark):
    # #         h, w, c = img.shape
    # #         cx, cy = int(lm.x * w), int(lm.y * h)
    # #         lmlist.append([id, cx, cy])
    # #         if mp_drawing:
    # #             cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
    # # if len(lmlist) != 0:
    # #     print(lmlist[4])
    #draw annotations on the image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #if results.multi_hand_landmarks:
        #for hand_landmarks in results.multi_hand_landmarks:
            #mp_drawing.draw_landmarks(img,hand_landmarks,connections=mp_hands.HAND_CONNECTIONS)


    cv2.imshow('Sheeesh', img)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()