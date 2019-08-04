#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# TurtleBot must have minimal.launch & amcl_demo.launch
# running prior to starting this script
# For simulation: launch gazebo world & amcl_demo prior to run this script

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import sys
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64
from std_msgs.msg import Float64MultiArray
global x
global a
global b
b = 0

class GoToPose():
    def __init__(self):

        self.goal_sent = False

	# What to do if shut down (e.g. Ctrl-C or failure)
	rospy.on_shutdown(self.shutdown)
	print("!")
	
	# Tell the action client that we want to spin a thread by default
	self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.loginfo("Wait for the action server to come up")
	print("2")

	# Allow up to 5 seconds for the action server to come up
	self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
	goal = MoveBaseGoal()
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

	# Start moving
        self.move_base.send_goal(goal)
        print("3")

	# Allow TurtleBot up to 60 seconds to complete task
	success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        print("4")
        rospy.sleep(1)
def callback(data):
       global pub1
       global pub2
       a=str(data.data)
       print (a)
       l=len(a)
       k=0
       x=a[0]
       i=1
       while(i<l):
           if(k==0):
             x=x+a[i]
             
           if(a[i]==' '):
             k=1
             break
           i=i+1
           print i
       #i=i+1
       y=a[i+1]
       i=i+2
       while(i<l-3):
           if(k==1):
             y=y+a[i]
             i=i+1
           
         
             
       print y
       x=float(x)
       if(a[l-2]=='-'):       
         x=-x
       print (x)
       y=float(y)
       if(a[l-1]=='-'):
         y=-y
       print y
       navigator = GoToPose()
       print("l")
       t=2
       i=0
       kk=['6.728 0.024++','5.846 3.647+-','4.150 3.339+-']
       r3=['0.672','0.074','-0.768']
       r4=['0.740','0.997','0.640']
       while(len(kk)>i):
            if(kk[i]==a):
              z1=np.float64(r3[i])
              z2=np.float64(r4[i])
            i=i+1
            
              
       while(t>0):
          position = {'x': x, 'y' : y}
          quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : z1, 'r4' : z2}

          rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
          success = navigator.goto(position, quaternion)
        
          if success:
             rospy.loginfo("Hooray, reached the desired pose")
             wow="1"
             wo=1
             print wow
             pub1.publish(wow)
             pub2.publish(wow)
             #pub3.publish(wo)
          else:
             rospy.loginfo("The base failed to reach the desired pose")
          t=t-1   

        # Sleep to give the last log messages time to be sent
          rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        global pub1
        rospy.init_node('nav_test', anonymous=True)
        print("7")
        rospy.Subscriber("/posision", String ,callback)
        print("6")
        pub1=rospy.Publisher("/key",String,queue_size=10)
        pub2=rospy.Publisher("/traff",String,queue_size=10)
        #pub3=rospy.Publisher("/kiss",Int64,queue_size=10)
        rospy.spin()
       
        
    except rospy.ROSInterruptException:
         rospy.loginfo("Ctrl-C caught. Quitting")
     
   
