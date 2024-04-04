# 🖐️ AI-Powered Virtual Mouse

Welcome to the AI-Powered Virtual Mouse project! This project uses hand gestures to control the mouse cursor. It leverages OpenCV for capturing video frames, MediaPipe for hand detection, and PyAutoGUI for controlling the mouse.

## 🎯 Features

- **Real-time Hand Detection:** The application captures video feed in real-time and detects hand movements.
- **Mouse Control:** You can control the mouse pointer using your index finger.
- **Click Action:** Perform click actions by bringing your thumb and index finger close together.

## 📦 Modules Used

- `cv2`: The OpenCV library is used for capturing video frames and image processing.
- `mediapipe`: Google's MediaPipe library is used for hand detection.
- `pyautogui`: This library allows for programmatically controlling the mouse.

## 🚀 How to Run

1. Ensure you have Python installed on your machine.
2. Install the necessary libraries using pip:

```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
```
##  🏃 Run The File

To run the file run the main python file mouse.py

## ⚠️ Remainder

Please note that the system is currently in the early stages of development and may not be fully optimized.

## 📚 For More Detail

For a detailed explanation of the code, please refer to the comments in the code files. Each line of code is explained to help you understand how the program works.

## 🚧 Future Work

Add support for more gestures and map them to different functions.
Improve hand detection accuracy and robustness.
Add support for custom gestures defined by the user.

## 🤝 Contributions

Contributions to this project are welcome! Please fork the repository and open a pull request with your changes.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.

## 🛠️ How It Works

The script starts by capturing video frames from the webcam using OpenCV. These frames are then passed to the hand detection model from the MediaPipe library. The model returns the positions of different landmarks on the hand. A yellow circle is drawn around the index finger and the thumb to show the position of the fingers being tracked. The script uses the position of the index finger to control the position of the mouse pointer. When the thumb and index finger come close together, a click action is performed.

!Hand Landmarks

The image above shows the landmark points in the hand which are used to detect the presence of the hand and also to control movement of the fingers.
