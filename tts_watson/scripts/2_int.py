#!/usr/bin/env python
import rospy
from std_msgs.msg import String

global word1
word1='whoisdevil'
global word2
word2='manuisdevil'
global sir
sir=0
global k
k=0
def akhilisback(data):
   print "ok1"
   global word1
   word1=data.data

def callback(data):
   global k
   global pub
   global pub1
   print "ok2"
   global word2
   global word1
   
   
   word2=data.data
   print "1"
   print word1
   print word2
   pqr="ack"

   if(word1==word2):
     st="yes "+word1+" is found"

     print st
     print pqr
#     pub.publish(st)
     print "bye bye"
     if(k==0):
       print "ok"
       pub.publish(st)

       pub1.publish(pqr)
       k=1
   #else:
    # st="yes "+word1+" is not found"
     #pub.publish(st)
     #pub1.publish(pqr)
     
def akhil(data):
#   rospy.Subscriber("/object",String,akhilisback) 
   print "hii"
   global k
   k=0
   rospy.Subscriber("/darknet_ros/found_obj",String,callback)
   #rospy.Subscriber("/object",String,akhilisback)
   rospy.spin()


def listener():
   global pub
   global pub1
   global word1
   global word2
   rospy.init_node('listener',anonymous=True)
   pub = rospy.Publisher('recognized_speech', String, queue_size=10)
   pub1 = rospy.Publisher('/traff',String,queue_size=10)
   rospy.Subscriber("/key",String,akhil)
   rospy.Subscriber("/object",String,akhilisback)
 #  rospy.Subscriber("/darknet_ros/found_obj",String,callback)
   print word1
   print word2
   if(word1==word2):
     st="yes "+word1+" is found"
     pqr="ack"
     pqr="ack2"
     print st
     print pqr
     pub.publish(st)
     pub.publish(pqr)
   rospy.spin()
if __name__ == '__main__':
   listener()
