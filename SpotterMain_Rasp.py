from motor_control import Motor
import keyboard as kb
#import JoystickModule as js
from time import sleep
#############################a##### SETTINGS
motor = Motor(17, 22, 27, 2, 3, 4,)
runCamera = False
movement = 'Keyboard' #[Keyboard, Joystick]
##################################

kb.init()

def main():
    #print(kb.getKey('s'))
    #motor.move(0.10, 0, 3.0)
    #motor.stop()

    if movement == 'Joystick':
        #print(js.getJS())
        sleep(0.1)
        #jsVal = js.getJS()
        #motor.move(-(jsVal['axis2']), -(jsVal['axis1']), 0.01)

    else:
        if kb.getKey('UP'):
            motor.move(0.45, 0, 0.1)
        elif kb.getKey('DOWN'):
            motor.move(-0.45, 0, 0.1)
        if kb.getKey('LEFT'):
            motor.move(0.5, -0.35, 0.1)
        if kb.getKey('RIGHT'):
            motor.move(0.5, 0.35, 0.1)
        else:
            motor.stop(0.1)

if __name__ == '__main__':
    while True:
        main()