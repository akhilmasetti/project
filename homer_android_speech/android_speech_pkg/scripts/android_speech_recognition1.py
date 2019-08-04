#!/usr/bin/python2.7
# socket skeleton from  http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
from thread import *
import rospy
from std_msgs.msg import String


recognized_speech_pub = rospy.Publisher('/recognized_speec', String, queue_size=10)
#recognized_speech_pub = rospy.Publisher('/decoded_msg', String, queue_size=10)

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
        #find the object in the roo        while(akhil[])
        recognized_speech_pub.publish(String(akhil))
        '''ls=['10.6 13.4--','13.0 0++','BAG','pasta','noodles']
        i=0
        word='NEW LAB'
        word1='OLD LAB'
        ak=len(akhil)-1
        k=0
        t=0
        
        #print(ord(akhil[7]))
        if(akhil=='NEW LAB'):
           print("ok new")
        while(i<len(word)):
             if(akhil[i]==word[i]):
               print("ok new")
               k=k+1
             i=i+1
        i=0
        while(i<len(word1)):
             if(akhil[i]==word1[i]):
               print("pppp")
               t=t+1
             i=i+1
        if(t==len(word1)):
           print('ok ok')
           recognized_speech_pub.publish(str(ls[1]))

        if(k==len(word)):
           print('ok ok')
           recognized_speech_pub.publish(str(ls[0]))
        

        while(i<len(ls)):
            words = akhil.split() #split the sentence into individual words
            print words
            if ls[i] in words:
                print 'jdfafo'
                recognized_speech_pub.publish(str(ls[i]))
                print 'jadvnjn'
            i=i+1'''
              
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
