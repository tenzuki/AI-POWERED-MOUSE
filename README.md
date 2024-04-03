# AI-Powered Virtual Mouse

This project is an AI-powered virtual mouse controlled using hand gestures. It uses OpenCV for capturing video frames, MediaPipe for hand detection, and PyAutoGUI for controlling the mouse.

## Features

- Hand detection in real-time video feed
- Control mouse pointer using index finger
- Perform click action by bringing thumb and index finger close

## Modules Used

- `cv2`: OpenCV library for capturing video frames and image processing
- `mediapipe`: Google's MediaPipe library for hand detection
- `pyautogui`: Library for programmatically controlling the mouse

## How to Run

1. Ensure you have Python installed on your machine.
2. Install the necessary libraries using pip:

## Command to install packages
1. pip install opencv-python
2. pip install mediapipe
3. pip install pyautogui

## To Run The Script
run the main file mouse.py

## Remainder
currently the system is not very optimized and is in the early stages of development

##Future Work
Add support for more gestures and map them to different functions.
Improve hand detection accuracy and robustness.
Add support for custom gestures defined by the user.

##Contributions
Contributions to this project are welcome! Please fork the repository and open a pull request with your changes.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.

##How It Works
The script starts by capturing video frames from the webcam using OpenCV.
These frames are then passed to the hand detection model from the MediaPipe library. The model returns the positions of different landmarks on the hand.
A yelllow circle is drawn around the index finger and the thumb finger to show the position of the fingers being tracked 
The script uses the position of the index finger to control the position of the mouse pointer. When the thumb and index finger come close together, a click action is performed.


![download](https://github.com/parthivk755/AI-POWERED-MOUSE/assets/66314611/bd554e86-ce82-461b-a3f9-de66ae34a8c6)

Image showing the landmark points in the hand which are used to detetct the presence of the hand and also to control movement of the fingers

##Future Work
Add support for more gestures and map them to different functions.
Improve hand detection accuracy and robustness.
Add support for custom gestures defined by the user.

##Contributions
Contributions to this project are welcome! Please fork the repository and open a pull request with your changes.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.
