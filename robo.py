import cv2
import numpy as np
import pyzbar.pyzbar as qr
from PIL import Image
import gpiozero
from gpiozero import Servo
import RPi.GPIO as GPIO
import pigpio
import time
from time import sleep

TRIG=23
ECHO=24
trigger=gpiozero.OutputDevice(TRIG)
echo=gpiozero.DigitalInputDevice(ECHO)
#====== in terminal type "sudo pigpiod" before running this !========
servo1 = 1 #put servo pin num
servo2 = 2
servo3 = 3
servo4 = 4
servo5 = 5
servo6 = 6

pwm = pigpio.pi() 

pwm.set_mode(servo1, pigpio.OUTPUT)
pwm.set_mode(servo2, pigpio.OUTPUT)
pwm.set_mode(servo3, pigpio.OUTPUT)
pwm.set_mode(servo4, pigpio.OUTPUT)
pwm.set_mode(servo5, pigpio.OUTPUT)
pwm.set_mode(servo6, pigpio.OUTPUT)

cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

pwm.set_PWM_frequency( servo1, 50 )
pwm.set_PWM_frequency( servo2, 50 )
pwm.set_PWM_frequency( servo3, 50 )
pwm.set_PWM_frequency( servo4, 50 )
pwm.set_PWM_frequency( servo5, 50 )
pwm.set_PWM_frequency( servo6, 50 )

robot=gpiozero.Robot(left=(22,27),right=(17,18))

def get_distance(trigger,echo):
    trigger.on()
    sleep(0.00001)
    trigger.off()

    while echo.is_active == False:
        pulse_start=time.time()

    while echo.is_active == True:  
        pulse_end=time.time()
  
    pulse_duration=pulse_end - pulse_start
    distance = 34300 * (pulse_duration/2)
    round_duration=round(distance,2)
    return(round_duration)

def capture():
    ret,frame = cap.read()
    flipped = cv2.flip(frame, flipCode=-1)
    frame1=cv2.resize(flipped,(640,480))
    qrdetect=qr.decode(frame1)
    return qrdetect

while True:
    qrdetect=capture()  
    distance_to_obj=get_distance(trigger,echo)

    for i in qrdetect:
        print("a")