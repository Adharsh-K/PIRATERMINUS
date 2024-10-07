# Program To Read video
# and Extract Frames
from re import S
import cv2
import os
import time

# Function to extract frames
def FrameCapture(path):
	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 1
	frames_extracted = 0

	# checks whether frames were extracted
	success, image=vidObj.read()
	THRESH = 30
	init_window = True
	curr_directory = "window_0"

	while success:

		if frames_extracted%10==0:
			# change directory
			curr_directory = f"window_{frames_extracted//10}"
		if os.path.isdir(curr_directory):
			pass
		else:
			os.mkdir(curr_directory)

		success, image = vidObj.read()

		if count%THRESH == 0 :
		    cv2.imwrite(f"{curr_directory}/frame{count}.jpg", image)
			frames_extracted += 1

		count += 1

# Driver Code
if __name__ == '__main__':

	# Calling the function
	FrameCapture("abc.mp4")
