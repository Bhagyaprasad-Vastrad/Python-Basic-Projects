{
 "cells": [
  {
   cell_type: "code",
   execution_count: null,
   metadata: {},
   outputs: [],
   source: [
    # OpenCV Python program to detect cars in video frame \n",
    # import libraries of python OpenCV  \n",
    import cv2 \n,
      \n,
    # capture frames from a video \n",
    cap = cv2.VideoCapture('video.avi') \n,
      \n,
    # Trained XML classifiers describes some features of some object we want to detect \n",
    car_cascade = cv2.CascadeClassifier('cars.xml') \n,
      \n,
    # loop runs if capturing has been initialized. \n",
    while True: \n",
        # reads frames from a video \n",
        ret, frames = cap.read() \n,
          \n,
        # convert to gray scale of each frames \n",
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) \n,
         \n,
      \n,
        # Detects cars of different sizes in the input image \n",
        cars = car_cascade.detectMultiScale(gray, 1.1, 1) \n,
        \n,
      # To draw a rectangle in each cars \n",
       for (x,y,w,h) in cars: \n,
           cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) \n,
      \n,
       # Display frames in a window  \n",
       cv2.imshow('video2', frames) \n,
          \n,
        # Wait for Esc key to stop \n",
        if cv2.waitKey(33) == 27: \n,
            break\n",
     # De-allocate any associated memory usage \n",
    cv2.destroyAllWindows() 
   ]
  }
 ],
 metadata: {
  kernelspec: {
   display_name: "Python 3",
   language: "python",
   name: "python3"
  },
  language_info: {
   codemirror_mode: {
    name: "ipython",
    version: 3
   },
   file_extension: ".py",
   mimetype: "text/x-python",
   name: "python",
   nbconvert_exporter: "python",
   version: "3.6.5"
  }
 },
 nbformat: 4,
 nbformat_minor: 2
}
