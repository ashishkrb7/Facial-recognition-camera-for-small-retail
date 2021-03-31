import cv2
import numpy as np
import os
	
modelFile = "models/res10_300x300_ssd_iter_140000.caffemodel"
configFile = "models/deploy.prototxt.txt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
images = os.listdir('faces')

for image in images:
    img = cv2.imread(os.path.join('faces', image))
    img = cv2.resize(img, None, fx=2, fy=2)
    height, width = img.shape[:2]
    img2 = img.copy()
    # detect faces in the image
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces3 = net.forward()
    #OPENCV DNN
    for i in range(faces3.shape[2]):
        confidence = faces3[0, 0, i, 2]
        if confidence > 0.5:
            box = faces3[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(img2, (x, y), (x1, y1), (0, 0, 255), 2)
  
    cv2.imshow("dnn", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()