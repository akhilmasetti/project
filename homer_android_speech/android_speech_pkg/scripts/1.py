#!/usr/bin/python2.7
# socket skeleton from  http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
from thread import *
import rospy
from std_msgs.msg import String
from datetime import datetime


recognized_speech= rospy.Publisher('/recognized_speech', String, queue_size=10)
recognized_speech_pub = rospy.Publisher('/decoded_msg', String, queue_size=10)

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
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
       
        
        akhil='my task is '+akhil
        #find the object in the roo        while(akhil[])
        recognized_speech.publish(String(akhil))
        ls1=['3.55 0.619+-','13.0 0++']
        ls=['BEDROM','TABLE','LIVING']
        i=0
        word='bedroom'
        word1='table'
	word2 = 'living room'
	ls2 = ['TIME']
	
        ak=len(akhil)-1
        
	
	print len(akhil)
	
	
	
        
        #print(ord(akhil[7]))
        
              
    #came out of loop
  

        while(i<len(ls)):
            words = akhil.split() #split the sentence into individual words
            print words
            if ls[i] in words:
                kkkk = 'I am going to'+ls2[i]
                print 'jdfafo'
                print ls1[i]
                asd=str(ls1[i])
                recognized_speech.publish(kkkk)
                print 'jadvnjn'
            i=i+1
        i = 0
        while(i<len(ls2)):
            words = akhil.split() #split the sentence into individual words
            print words
            print "hii"
            if ls2[i] in words:
                
                #recognized_speech.publish(String(akhil))
                currentDT = datetime.now()
                print 'jdfafo'
                print (str(currentDT))
                ad=str(currentDT)
                ad='3.55 0.619+-'
                recognized_speech_pub.publish(ad)
                print 'jadvnjn'
            i=i+1
              
    #came out of loop
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
