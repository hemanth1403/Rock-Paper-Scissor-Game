# Hand Gesture Game

This project is a hand gesture-based game built using OpenCV, cvzone, and a hand detection module. The game allows a player to compete against the computer using hand gestures.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- cvzone
- A webcam

## Installation

1. Install the necessary libraries:

   ```bash
   pip install opencv-python cvzone
   ```

2. Make sure you have a webcam connected to your computer.

## How to Run

1. Save the code in a Python file (e.g., `hand_game.py`).

2. Ensure you have the required images in the `Inventory` folder:

   - `BackGround.png`: The background image.
   - `1.png`: Image representing gesture 1.
   - `2.png`: Image representing gesture 2.
   - `3.png`: Image representing gesture 3.

3. Run the Python file:

   ```bash
   python hand_game.py
   ```

4. Press the "s" key to start the game.

## How to Play

- The game captures the hand gestures using the webcam.
- The player can make one of three gestures:
  - All fingers down (representing gesture 1).
  - All fingers up (representing gesture 2).
  - Index and middle fingers up (representing gesture 3).
- The computer randomly chooses a gesture.
- The scores are updated based on the player's gesture and the computer's choice.

## Code Overview

### Libraries and Initialization

```python
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
```

- random: For generating random gestures for the computer.
- cv2: For image processing and video capture.
- cvzone: For overlaying images.
- HandDetector: From cvzone for detecting hand gestures.
- time: For handling the game timer.

### Setup

```python
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0, 0]
```

- cap: Captures video from the webcam.
- detector: Initializes hand detector to detect one hand.
- timer, stateResult, startGame, scores: Game state variables.

### Game Loop

```python
while 1:
    imageBG = cv2.imread("Inventory/BackGround.png")
    success, img = cap.read()

    imgScale = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScale = imgScale[:, 80:480]

    hands, img = detector.findHands(imgScale)

```

- Reads the background image and captures the video frame.
- Resizes and crops the video frame.
- Detects hand gestures.

### Game Logic

```python
    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imageBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer > 3:
                stateResult = True
                timer = 0
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3
                    queryAI = random.randint(1, 3)
                    imgAI = cv2.imread(f"Inventory/{queryAI}.png", cv2.IMREAD_UNCHANGED)
                    imageBG = cvzone.overlayPNG(imageBG, imgAI, (149, 310))
                    if playerMove == queryAI:
                        pass
                    elif (playerMove == 1 and queryAI == 2) or (playerMove == 2 and queryAI == 3) or (playerMove == 2 and queryAI == 1) or (playerMove == 3 and queryAI == 2):
                        scores[1] += 1
                    else:
                        scores[0] += 1

```

- Handles the game logic and updates scores based on gestures.

### Display and Key Handling

```python
    imageBG[234:654, 795:1195] = imgScale
    if stateResult:
        imageBG = cvzone.overlayPNG(imageBG, imgAI, (149, 310))
    cv2.putText(imageBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imageBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("ImageBG", imageBG)
    key = cv2.waitKey(2)
    if key == ord("s"):
        startGame = True
        initialTime = time.time()
        stateResult = False

```

- Updates the background image with the game state.
- Displays the scores and the video feed.
- Starts the game on pressing the "s" key.
