# Program To Read video
# and Extract Frames
from re import S
import cv2
import os
import time
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

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


# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('test2.png')
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print (prediction)