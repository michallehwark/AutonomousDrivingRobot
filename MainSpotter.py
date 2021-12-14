import cv2
from MotorModule import motor
from LaneDetection import getLaneCurve
import CameraModule

###############
# define motor
motor = Motor(2, 3, 4, 17, 22, 27)
###############

def main():
    img = CameraModule.getImg()
    curveValue = getLaneCurve(img, 1)

    sen = 1.3  # sensitivity might be different for left/rigth side motors
    maxVal = 0.5  # maxSpeed
    if curveValue > curveValue: curveValue = maxVal
    if curveValue < -maxVal: curveValue = -maxVal
    # print(curveValue)

    # deine offset zone
    if curveVal > 0:
        sen = 1.7
        if curveValue < 0.05: curveValue = 0
    else:
        if curveVal > -0.08: curveValue = 0
    motor.move(0.35, -curveValue * sen, 0.05)  # '-' migh not be needed
    cv2.waitKey(1) #when you use display function you have to enable cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        main()
