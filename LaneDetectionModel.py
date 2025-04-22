import cv2
import numpy as np
import utils

def getlaneCurve(img, display=False):
    imgThres = utils.thresholding(img)
    h ,w,c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpImg(img, points, w, h)
    imgWarpPoints = utils.drawPoints(imgWarp, points)
    cv2.imshow("imgThres", imgThres)
    cv2.imshow("imgWarp", imgWarp)
    cv2.imshow("imgWarpPoints", imgWarpPoints)
    return None



if __name__ == "__main__":
    cap = cv2.VideoCapture("vid1.mp4")
    initialTrackbarVals = [100, 100, 100, 100]
    utils.initializeTrackbars(initialTrackbarVals)

    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        sucess, img  = cap.read()
        if not sucess:
            break
        img = cv2.resize(img, (640, 480))
        getlaneCurve(img, display=True) 

        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        


        
            