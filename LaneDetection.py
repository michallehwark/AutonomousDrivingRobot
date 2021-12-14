import cv2
import numpy as np
import utilities
curveList = []
avgVal = 10
def getLaneCurve(img, display = 2): #display=0(displays nothing), display=1(displays result), display=2(displays transition)

    imgCopy = img.copy()
    imgResult = img.copy()
#   Step 1
    imgThresh = utilities.threshholding(img)

#   Step 2
    hT, wT, c = img.shape
    points = utilities.valTrackbars()
    imgWarp = utilities.warpImg(imgThresh, points, wT, hT)
    imgWarpPoints = utilities.drawPoints(img, points)

#   Step 3
    midPoint,imgHist = utilities.getHistogram(imgWarp, minPer = 0.5, display = True, region = 4)
    curveAveragePoint,imgHist = utilities.getHistogram(imgWarp, minPer = 0.9, display = True, region = 1)
    curveRaw = curveAveragePoint - midPoint

    #   Step 4
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop((0))
    curve = int(sum(curveList)/len(curveList))

    #   Step 5
    if display != 0:
        imgInvWarp = utilities.warpImg(imgWarp, points, wT, hT, inverse = True)
        imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT//3,0:wT] = 0,0,0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
        midY = 450
        cv2.putText(imgResult,str(curve),(wT//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
        cv2.line(imgResult,(wT//2,midY),(wT//2+(curve*3),midY),(255,0,255),5)
        cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY-25), (wT // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
                     (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)
#        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
#        cv2.putText(imgResult, 'FPS '+str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,50,50), 3);
    if display == 2:
        imgStacked = utilities.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                            [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)

    # check values of the curve and normalise them
    curve = curve/100
    if curve > 1 : curve == 1
    if curve < -1 : curve == -1

    #cv2.imshow('Treshhold', imgThresh)
    #cv2.imshow('Warp', imgWarp)
    #cv2.imshow('imgWarpPoints', imgWarpPoints)
    #cv2.imshow('Histogarm', imgHist)
    return curve


if __name__ == '__main__':
    cap = cv2.VideoCapture('film.mov')
    initialTracBarValues = [102, 80, 20, 214]
    utilities.initTrackbars(initialTracBarValues)
    frameCounter = 0
    while True:
        frameCounter += 1
        ile = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:#+ 30:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
            frameCounter = 0

        _, img = cap.read()
        img = cv2.resize(img, (480, 240))
        curve = getLaneCurve(img, display = 2)
        print(curve)
        #cv2.imshow('Vid', img)
        cv2.waitKey(10)
