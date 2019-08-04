#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from std_msgs.msg import Int64
import time

global obj_id


def obj_id(data):
    global obj_id
    obj_id=float(data.data)
    print obj_id


def feedback(msg):
    global pub
    global t
    global pub3
    asd=1
    print msg.orientation.x
    if(msg.orientation.x==obj_id):
      pub3.publish(asd)
      msg1=Pose()
      msg1.position.x=msg.position.x
      msg1.position.y=msg.position.y
      msg1.position.z=msg.position.z
      #if(t==0):
      pub.publish(msg1)
      time.sleep(20)
       # t=1
    


def callback(data):
    global t
    global msg
    msg=Pose()
    t=0
    rospy.Subscriber('darknet_ros/points',Pose,feedback)
    rospy.spin()



def arm():
    global pub
    global pub3
    rospy.init_node('img_arm')
    rospy.Subscriber('/key',String,callback)
    pub=rospy.Publisher('/to_arm',Pose,queue_size=10)
    pub3=rospy.Publisher('/kiss',Int64,queue_size=10)
    rospy.Subscriber('/obj_id',String,obj_id)
    rospy.spin()
if __name__ == '__main__':
    arm()
