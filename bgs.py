import numpy as np
import cv2
import argparse

# Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', required=True, help='Path to image file')
ap.add_argument('-w', '--width', type=int, default=0,
    help='Width to resize image to in pixels')
ap.add_argument('-n', '--num-clusters', type=int, default=3,
    help='Number of clusters for K-means clustering (default 3, min 2).')
args = vars(ap.parse_args())

if not args.get('video', False):
    # Read video file into a VideoCapture object
    cap = cv2.VideoCapture(args['video'])
else:
    # Read video from webcam
    cap = cv2.VideoCapture(0)

# Check if file/webcam was accessed successfully
if (cap.isOpened()== False):
  raise Exception('Error opening video file / accessing webcam.')

# Create MOG2 background subtractor 
fgbg = cv2.createBackgroundSubtractorMOG2(history=300,varThreshold=16,detectShadows=False)

while(cap.isOpened()):
    ret, frame = cap.read()

    # Apply background subtraction to produce mask
    fgmask = fgbg.apply(frame)

    # Create and resize windows
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.namedWindow('fgmask',cv2.WINDOW_NORMAL)

    if args['width'] > 0:
        height = int((args['width'] / image.shape[1]) * image.shape[0])
        cv2.resizeWindow('frame',args['width'],height)
        cv2.resizeWindow('fgmask',args['width'],height)

    # Perform K-means clustering
    if args['num_clusters'] < 2:
        print('Warning: num-clusters < 2 invalid. Using num-clusters = 2')
    numClusters = max(2, args['num_clusters'])
    
    
    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
