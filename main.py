import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time


cap = cv2.VideoCapture(0)
cap.set(3, 640) # 3 -> Width
cap.set(4, 480) # 4 -> Height

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0,0]

while 1:
    imageBG = cv2.imread("Inventory/BackGround.png")
    success, img = cap.read()

    imgScale = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScale = imgScale[:, 80:480]

    hands, img = detector.findHands(imgScale)

    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imageBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer>3:
                stateResult = True
                timer = 0
                # imgAI=None
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if(fingers == [1, 1, 1, 1, 1]):
                        playerMove = 2
                    if(fingers == [0, 1, 1, 0, 0]):
                        playerMove = 3
                    print(fingers)
                    queryAI = random.randint(1,3)
                    imgAI = cv2.imread(f"Inventory/{queryAI}.png", cv2.IMREAD_UNCHANGED)
                    imageBG = cvzone.overlayPNG(imageBG, imgAI, (149, 310))
                    if playerMove==queryAI:
                        pass
                    elif (playerMove==1 and queryAI==2) or (playerMove==2 and queryAI==3) or (playerMove==2 and queryAI==1) or (playerMove==3 and queryAI==2):
                        scores[1]+=1
                    else:
                        scores[0]+=1
    imageBG[234:654, 795:1195] = imgScale
    if stateResult:
        imageBG = cvzone.overlayPNG(imageBG, imgAI, (149, 310))
    cv2.putText(imageBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imageBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # cv2.imshow("Image", img)
    cv2.imshow("ImageBG", imageBG)
    # cv2.imshow("Scale", imgScale)
    key = cv2.waitKey(2)
    if key == ord("s"):
        startGame = True
        initialTime = time.time()
        stateResult = False