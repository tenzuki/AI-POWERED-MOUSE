""" an ai powered virtual mouse controlled using our finger tips """

# step 1:- capture the video frames using opencv

import cv2                                     # opencv2 is a module which is related to computer vision and helps us to do operations based upon a camera

#step 2:- detect the hand from the frames captured

import mediapipe as mp                         # meadiapipe is an exterernal module which is powered by google for detetecting 

#step 3:- control the mouse using the index finger

import pyautogui                               # pyautogui is a module which helps with controlling the various aspects of the system and interact with them 

cap = cv2.VideoCapture(0)                      # this line starts to record the video from the camera 0 = front camera 1 = rear camera 

hand_detector = mp.solutions.hands.Hands()     # we are using the  mediapipe module to detect the hand from the frames 
drawing_utils = mp.solutions.drawing_utils     # we are plotting out the landmarks of the hand
screen_width, screen_height = pyautogui.size() # taking out the screen size of the respective system 
index_y = 0                                    # setting the initial position value of the top most part of the index finger 

while True:                                    # opening a continous loop for the capturing of the hand

    _, frame = cap.read()                      # reading all the frames from the camera
    frame = cv2.flip(frame, 1)                 # by default the opencv mirorrs the image infront of the cameea by giving the vakue 1 we are flipping the image read from the camera
    frame_height, frame_width, _ = frame.shape # setting the up the frame size of the capture window
    rgb_frmae = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # converting the colour scale of the frames captured from RGB2BGR for the smoothness of processing the frames
    output = hand_detector.process(rgb_frmae)  # passing the convert colour scales frames to the hand detector method tho detect the hands
    hands = output.multi_hand_landmarks        # setting up the landmarks on the fingers of the hands
    if hands:                                  # conditon statement for checking the presence of hand in the frame 
        for hand in hands:                     # a for loop to continously iterate and check for hand in the hands method 
            drawing_utils.draw_landmarks(frame, hand) # drawing the landmarks on each frame captuted from the capture window
            landmarks = hand.landmark          # setting the value of the landmark points in the hand
            for id,landmark in enumerate(landmarks): # for loop for giving position values to each landmark enumerate means to move through the whole landmarks in the hand
                x = int(landmark.x*frame_width)      # adjusting the position values of the pointer landmark for x axis and called it as an integer to get a whole number 
                y = int(landmark.y*frame_height)     # adjusting the position values of the pointer landmark for y axis and called it also an integer to get a whole number    

                # tracking the position of the index finger and pointer 

                if id == 8:                    # 8 is the position value of the index finger the index finger is used to track the movement of the pointer 
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255)) # we are drawing a cirlce to showcase the position of the top most part of the indrex finger 
                    index_x = screen_width/frame_width*x # adjusting the size of the x axis to the whole screen 
                    index_y = screen_height/frame_height*y # adjusting the size of the y axis to the whole screen 
                    pyautogui.moveTo(index_x, index_y) # initializing the pyautogui module to move the pointer according to the position of the index finger

                # tracking the position of the thumb to do the click action 

                if id == 4:                     # 4 is the position value of the thumb finger and is used to replicate the action of a click
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255)) # drawingf a circle aroung the thump finger 
                    thumb_x = screen_width/frame_width*x # adjusting the size of the x axis of the thumb 
                    thumb_y = screen_height/frame_height*y #adjusting the size of the y axis of the thumb
                    print('diff',abs(index_y - thumb_y))  # an erorr handling statement to check the difference between the thumb and the index finger 
                    if abs(index_y - thumb_y) < 20: # if the difference between the index and thumb is below 20 position value then it replicates the click action
                        print("click") # prints statment to show click whenever a clcik is activated by the system 
                        pyautogui.click() # initializing the pyautogui to do the clck action 
                        pyautogui.sleep(1) # after initiating a single click response the next click is only done after a second to filter out accidental clicks
    cv2.imshow(" MADE BY PARTHIV ", frame) # to show the capture window and see the real time tracking and movemet of the hand 
    cv2.waitKey(1) # a timer function to wait for 1 second to reduce the buffering of frames captured 