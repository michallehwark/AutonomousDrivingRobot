import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, Ena_A, In1_A, In2_A, Ena_B, In1_B, In2_B):
        #define for motor A
        self.Ena_A = Ena_A
        self.In1_A = In1_A
        self.In2_A = In2_A

        #define for motor B
        self.Ena_B = Ena_B
        self.In1_B = In1_B
        self.In2_B = In2_B

        GPIO.setup(self.Ena_A, GPIO.OUT)
        GPIO.setup(self.In1_A, GPIO.OUT)
        GPIO.setup(self.In2_A, GPIO.OUT)
        GPIO.setup(self.Ena_B, GPIO.OUT)
        GPIO.setup(self.In1_B, GPIO.OUT)
        GPIO.setup(self.In2_B, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.Ena_A, 100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(self.Ena_B, 100);
        self.pwmB.start(0);


    def move(self, speed=0.40,turn=0, duration=0): #if user does not define speed or duration it'll use default
        speed *= 100
        turn *= 100
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        #        if turn != 0:
        #            if turn > 0 :
        #                rightSpeed = 0
        #                leftSpeed = turn
        #            else:
        #               rightSpeed = -turn
        #               leftSpeed = 0

        if leftSpeed>100: leftSpeed=100
        elif leftSpeed<-100: leftSpeed=-100
        if rightSpeed>100: rightSpeed=100
        elif rightSpeed<-100: rightSpeed=-100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed>0:
            GPIO.output(self.In1_A, GPIO.HIGH)
            GPIO.output(self.In2_A, GPIO.LOW)
        else:
            GPIO.output(self.In1_A, GPIO.LOW)
            GPIO.output(self.In2_A, GPIO.HIGH)

        if rightSpeed>0:
            GPIO.output(self.In1_B, GPIO.HIGH)
            GPIO.output(self.In2_B, GPIO.LOW)
        else:
            GPIO.output(self.In1_B, GPIO.LOW)
            GPIO.output(self.In2_B, GPIO.HIGH)

        sleep(duration);

    def stop(self, t=2):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(t)

def main():
    motor.move(0.3, 0, 2)
    motor.stop()
    #motor.moveF(10, 3)
    #motor.stop(3)

if __name__ == '__main__':
    motor = Motor(2, 3, 4, 17, 22, 27)
    main()