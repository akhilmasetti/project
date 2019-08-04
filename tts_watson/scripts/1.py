#!/usr/bin/env python
import rospy
from std_msgs.msg import String

global word1
word1='devil'
global word2
word2='manuisdevil'

def akhilisback(data):
   print "ok1"
   global word1
   word1=data.data

def callback(data):
   global pub
   print "ok2"
   global word2
   word2=data.data
   print word1
   print word2
   if(word1==word2):
     st="yes "+word1+" is found"
     print st
     pub.publish(st)
   else:
     st="yes "+word1+" is not found"
     pub.publish(st)
     



def listener():
   global pub
   global word1
   global word2
   rospy.init_node('listener',anonymous=True)
   pub = rospy.Publisher('recognized_speech', String, queue_size=10)
   rospy.Subscriber("/recognized_speech",String,akhilisback)
   rospy.Subscriber("/darknet_ros/found_obj",String,callback)
   print word1
   print word2
   if(word1==word2):
     st="yes "+word1+" is found"
     print st
     pub.publish(st)
   rospy.spin()
if __name__ == '__main__':
   listener()
