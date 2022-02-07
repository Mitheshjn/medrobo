import cv2
import numpy as np
import pyzbar.pyzbar as qr
from PIL import Image
import gpiozero
from gpiozero import Servo
import time
from time import sleep
import serial

TRIG=18
ECHO=24
trigger=gpiozero.OutputDevice(TRIG)
echo=gpiozero.DigitalInputDevice(ECHO)
#====== in terminal type "sudo pigpiod" before running this !========

cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

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

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.reset_input_buffer()
  

  while True:
    ret,frame = cap.read()
    #flipped = cv2.flip(frame, flipCode=-1)
    frame1=cv2.resize(frame,(640,480))
    qrdetect=qr.decode(frame1)
    dist = get_distance(trigger,echo)
    #(dist)
    #distance_to_obj=get_distance(trigger,echo)
    if (dist<=15):
      ser.write(b"S")
      print("s")

    #======print(qrdetect)
    #======print(qrdetect[0].data.decode("ascii"))
    for i in qrdetect:
      #print (i.rect.left,i.rect.top,i.rect.width,i.rect.height)
      #print(i.data[0])
      
      if (i.data[0]==115 and i.data[1]==116 and i.data[2]==97 and i.data[3]==114 and i.data[4]==116):
        print("start")
        ser.write(b"F")
          
      elif (i.data[0]==119 and i.data[1]==49):
        print("w1")
        ser.write(b"R")
        time.sleep(1.25)
        ser.write(b"F")
        time.sleep(2.5)
        ser.write(b"S")
        
        if (i.data[3]==98 and i.data[4]==49):
          ser.write(b"F")
          time.sleep(2)
          ser.write(b"L")
          time.sleep(1.25)
          ser.write(b"S")

        elif (i.data[3]==98 and i.data[4]==49):
          ser.write(b"F")
          time.sleep(5)
          ser.write(b"L")
          time.sleep(1.25)
          ser.write(b"S")

      elif (i.data[0]==98 and i.data[1]==49):
        print("b1")
        ser.write(b"L")
        time.sleep(1.25)
        ser.write(b"S")
        #start servo mechanism for med distribution

      elif (i.data[0]==98 and i.data[1]==50):
        print("b2")
        ser.write(b"L")
        time.sleep(1.25)
        ser.write(b"S")
        #start servo mechanism for med distribution

      cv2.rectangle(frame1,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,255,0),3)
      cv2.putText(frame1,str(i.data),(20,20),font,2,(255,0,0),2) 

    cv2.imshow("Frame", frame1)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
      #cv2.waitKey(0)
      cv2.destroyAllWindows()
      break