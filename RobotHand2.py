import cv2
from cvzone.HandTrackingModule import HandDetector
import elevenlabs
from elevenlabs import generate, play, voices
from elevenlabs import set_api_key

set_api_key("f9c97646ef9d171b94b4c22fa5c7b9be")
voices = voices()
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
last = 0
commandNum = [0, 0, 0, 0, 0]
fingerNumNew = 0
fingerNumLast = 0

def speech(fingerN):
    if fingerN == 1:
        audio = generate(
            text="This is 1 finger",
            voice="OldIndian",
            model="eleven_monolingual_v1"
        )
    else:
        finger = "This is " + str(fingerN) + " fingers"
        print("test")
        audio = generate(
            text=finger,
            voice="OldIndian",
            model="eleven_monolingual_v1"
        )
    play(audio)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
        for i in range(5):
            if fingerup[i] == 1:
                fingerNumNew += 1
        if fingerNumNew == fingerNumLast:
            fingerNumNew = 0
        else:
            speech(fingerNumNew)
            fingerNumLast = fingerNumNew
            fingerNumNew = 0
            #print(fingerup)
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()