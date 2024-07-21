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
