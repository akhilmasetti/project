#!/usr/bin/python2.7
# socket skeleton from  http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
from thread import *
import rospy
from std_msgs.msg import String


recognized_speech_pub = rospy.Publisher('/akhil', String, queue_size=10)
pub=rospy.Publisher('/speech', String, queue_size=10)
#pub=rospy.Publisher('/decoded_msg',String, queue_size=10)
#pub1=rospy.Publisher('/person',String, queue_size=10)
#pub2=rospy.Publisher('/vas',String, queue_size=10	)
global temp
temp=0
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
    global temp
    while True:
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        print "Receiving recognition "+data
        i=0
        akhil=''
        while(data[i]!='\n'):
            akhil=akhil+data[i]
            i=i+1
            print "1"
        print akhil
        akhil=str(akhil)
        akhil=akhil[0:(len(akhil)-1)]
        print "hello"
        #find the object in the roo        while(akhil[]) 
        if(temp==0):
          recognized_speech_pub.publish(str(akhil))
          print "hiii"
          temp=1
        elif(temp==1):
          pub.publish(akhil)

           
    conn.close()

rospy.init_node('android_speech_recognition_node')
rospy.loginfo("android speech recognition node initialized")


host = rospy.get_param("~host","")   # Symbolic name meaning all available interfaces
port = int(rospy.get_param("~port","8051"))  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((host, port))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'


while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
s.close()
