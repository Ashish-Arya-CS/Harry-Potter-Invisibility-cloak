import cv2
import numpy as np
import time
#Here we import all the necessary libraries which includes opencv,numpy and time.

print("Launching invisibility cloak")

#accessing our laptop's webcam using this command which creates object cam.
cam = cv2.VideoCapture(0)

time.sleep(3)
background = 0

#reading the background video or series of images.
for i in range(50):
    ret, background = cam.read()

background = np.flip(background, axis=1)

#use a while loop since video is nothing but series of images.
while (cam.isOpened()):
    ret, img = cam.read()

    # Flipping the image along the axis=1.
    img = np.flip(img, axis=1)

    # Converting image to HSV color space using this command.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    
    #adding gaussian blur to the image.
    blurred = cv2.GaussianBlur(hsv, value, 0)
    
    # Defining lower range for red color detection.
    #detection of slightly lighter red in this range.
    # Defining Hue,Saturation,Value for red color that is present in this range.
    lower_red = np.array([0, 70, 40])
    upper_red = np.array([10, 255, 255])
    
    #creating a mask in the range specified.
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Defining upper range for red color detection
    #detection of slightly darker red in this range.
    lower_red = np.array([170, 90, 90])
    upper_red = np.array([180, 255, 255])
    
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Addition of the two masks to generate the final mask that includes all the shades from light to dark red.
    mask = mask1 + mask2
    
    # Refining the mask corresponding to the detected red color 
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    # Replacing pixels corresponding to cloak with the background pixels.
    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
