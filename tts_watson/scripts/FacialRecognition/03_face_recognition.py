import cv2
import numpy as np
import os 
import rospy
import time
from std_msgs.msg import String
from datetime import datetime
global a
global i
i=0
#a=['','','']
a=0
def waste(data):
   global pub
   global pub1
   global pub2
   k=0
   recognizer = cv2.face.LBPHFaceRecognizer_create()
   recognizer.read('trainer/trainer.yml')
   cascadePath = "haarcascade_frontalface_default.xml"
   faceCascade = cv2.CascadeClassifier(cascadePath);
   font = cv2.FONT_HERSHEY_SIMPLEX
   #iniciate id counter
   id = 0
   # names related to ids: example ==> Marcelo: id=1,  etc
   names = ['None', 'AKHIL', 'Paula', 'Ilza', 'Z', 'W'] 
   # Initialize and start realtime video capture
   cam = cv2.VideoCapture(0)
   cam.set(3, 640) # set video widht
   cam.set(4, 480) # set video height
   # Define min window size to be recognized as a face
   minW = 0.1*cam.get(3)
   minH = 0.1*cam.get(4)
   while True:
     ret, img =cam.read()
     img = cv2.flip(img, 1) # Flip vertically
     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
     faces = faceCascade.detectMultiScale( 
         gray,
         scaleFactor = 1.2,
         minNeighbors = 5,
         minSize = (int(minW), int(minH)),
        )
     for(x,y,w,h) in faces:
         
	 cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
         id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
         # Check if confidence is less them 100 ==> "0" is perfect match 
         if (confidence < 100):
             id = names[id]
             print id
             print "okok"
             print data
             if(data.data==id):
               if(k==0):
                  currentDT = datetime.now()
                  ad=str(currentDT)
                  #ad='time is '+ad
                  ad="yes "+id+" is found"
                  pqr="acknow"
                  k=1
                  pub.publish(ad)
                  pub2.publish(pqr)
              #time.sleep(10)
             #ads='0.27 0.58--'
             #pub1=publish(ads)
               
             #break
             confidence = "  {0}%".format(round(100 - confidence))
         else:
             id = "unknown"
             confidence = "  {0}%".format(round(100 - confidence))
         if(k==1):
           break
         cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
         cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
     cv2.imshow('camera',img) 
     k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
     if k == 27:
         break
  # Do a bit of cleanup
   cv2.destroyAllWindows()
   print("\n [INFO] Exiting Program and cleanup stuff")

def what(data):
   global a
   global i
   global k1
   a=data.data
   k1=1
def whatis():
   global a
   global k1
   if(k1==1):
     waste(a[i])
   


def li():
    rospy.init_node('whatisthis',anonymous=True)
    #pub1=rospy.Publisher('/decoded_msg',String,queue_size=10)
    rospy.Subscriber('/person',String,waste)
    global pub
    global pub2
    pub=rospy.Publisher('/recognized_speech',String,queue_size=10)
    pub2=rospy.Publisher('/face',String,queue_size=10)
    rospy.spin()

if __name__=='__main__':
   li() 
   #cap.release()

