import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)