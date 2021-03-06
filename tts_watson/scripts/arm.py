#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from std_msgs.msg import Int64
import time

global obj_id
global sh
#sh=['h','h','h','h','h','h','h','h','h','h','h','h','h','h','s','s','s','s','s','h','h','h','h','h','h','s','h','s','s','h','s','s','h','h','s','h','s','h','h','h','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s','h','h','h','h','h','h','h','h','h','h','s','h','h','s','h','h','h','h','s','s','s','s','s']


def obj_id(data):
    global obj_id
    obj_id=float(data.data)
    print obj_id


def feedback(msg):
    global pub
    global t
    global pub3
    global sh
    global pub2
    asd=1
    global obj_id
    print obj_id  
    print msg.orientation.x
    if(msg.orientation.x==obj_id):
      #b=int(obj_id)
      s='s'
      pub2.publish(s)
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
    global data
    global pub3
    global pub2
    data=Int64()
    rospy.init_node('img_arm')
    rospy.Subscriber('/key',String,callback)
    pub=rospy.Publisher('/to_arm',Pose,queue_size=10)
    pub3=rospy.Publisher('/kiss',Int64,queue_size=10)
    pub2=rospy.Publisher('/sh',String,queue_size=10)
    rospy.Subscriber('/obj_id',String,obj_id)
    rospy.spin()
if __name__ == '__main__':
    arm()
