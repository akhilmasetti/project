#!/usr/bin/python2.7


import rospy
from std_msgs.msg import String
import time
global k
k=0

def speech(data):
    global k
    global pub1    
    if(k==0):
      time.sleep(2)
      pub1.publish(data.data)
      k=1


def answer(data):
    global k
    global pub
    k=0
    ask="ask me a question"
    pub.publish(ask)
    #time.sleep(2)
    rospy.Subscriber("/speech",String,speech)
    rospy.spin()



def okok():
   global pub
   global pub1
   rospy.init_node('chatter',anonymous=True)
   rospy.Subscriber('/face',String,answer)
#   rospy.Subscriber("/speech",String,speech)
   pub=rospy.Publisher('/recognized_speech',String,queue_size=10)
   pub1=rospy.Publisher('/decoded_msg',String,queue_size=10)
   rospy.spin()
   

if __name__=='__main__':
  okok()


