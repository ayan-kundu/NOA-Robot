# testing the gripper

#Example Servo Code Control the angle of a 
#Servo Motor with Raspberry Pi  www.learnrobotics.org

# import GPIO AND Sleep
import RPi.GPIO as GPIO
from time import sleep
from pynput import keyboard
# setup GPIO rather Boardchannel(GPIO names GPIO 17=11 ON BOARD)
servo_pin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
#SETTING PWM 50Hz
pwm=GPIO.PWM(servo_pin, 50)
pwm.start(0)

duty = 2.22 # (4/18)+2 : angle / 18 + 2 # Move 4 degree 
duty_0=7.5 # % at 0 degree
duty_90=12 # % at +90 degree 2.5 @ -90 degree

#implement the duty to servo 
#GPIO.output(12, True)
pwm.ChangeDutyCycle(duty)
sleep(1)
print('duty cycle',duty_0,' at 0 degree')
pwm.stop()

# Find out degree to full open and close / set that as default or resting pose
# Gripper set to rest


# Gripper open 


# Gripper closed
# set to 5 deg = close // there should be a little gap in the claw when closed

