#Example Servo Code Control the angle of a 
#Servo Motor with Raspberry Pi  www.learnrobotics.org

# import GPIO AND Sleep
import RPi.GPIO as GPIO
from time import sleep
from pynput import keyboard
# setup GPIO rather Boardchannel(GPIO names GPIO 17=11 ON BOARD)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
#SETTING PWM 50Hz
pwm=GPIO.PWM(11, 50)
pwm.start(0)

#Function to convert angle to DutyCycle
def setAngle(angle,pin):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(duty)
# Function to select target servo
def servo1(setAngle):
    print('set to ', angle, ' deg')
    setAngle(0,12)
    sleep(1)

servo_num,angle=input('enter name of the servo and angle to rotate with space').split()

while True:
    if servo_num ==1:
        servo1()
    else:
        break

    if keyboard.is_pressed('q'):
        print('servo interrupted')
        pwm.stop()
        GPIO.cleanup()
