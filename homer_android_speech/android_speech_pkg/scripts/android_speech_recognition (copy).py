#!/usr/bin/python2.7
# socket skeleton from  http://www.binarytides.com/python-socket-server-code-example/

import socket
import sys
from thread import *
import rospy
from std_msgs.msg import String


recognized_speech_pub = rospy.Publisher('/akhil', String, queue_size=10)
#pub=rospy.Publisher('/decoded_msg',String, queue_size=10)
#pub1=rospy.Publisher('/person',String, queue_size=10)
#pub2=rospy.Publisher('/vas',String, queue_size=10	)

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
	'''sen = akhil
	v=['GET','GRASP','TAKE','PICK UP','DELIVER','PUT','PLACE','TELL','SAY','GO','NAVIGATE','ENTER','FIND']
	pl=['EXIT','TABLE','COUNTER','KITCHEN','BEDROOM','LIVING','CORRIDOR','OFFICE','DINNING','BAR','SINK','','']
	obj=['PRINGLES','IT','APPLE','CRACKERS','COKE','TEA','BEER','BISCUITS','SOAP','','','','']
        per=['','','','','','','','','','','','','']
	po =['','','']
        i=0
        
        
	j=0
	k=0
	verbs=['','','']
	place=['','','']
	person=['','','']
	vas=['','','']
	print len(words)
	while(i<len(words)):
   		j=0
    	while(j<len(v)):
       
        	if(words[i]==v[j]):
         
         		verbs[k]=words[i]
         		
         		k=k+1
         		break
       		j=j+1
    		print i   
    		i=i+1
 
	i=0	
	k=0

	while(i<len(words)):
    		j=0
    	while(j<len(pl)):
       
       		if(words[i]==pl[j]):
         
         		place[k]=words[i]
         		
         		k=k+1
         		break
       		j=j+1
    		print i   
    		i=i+1 


  
	i=0
	k=0

	while(i<len(words)):
    		j=0
    	while(j<len(obj)):
       
       		if(words[i]==obj[j]):
         
         		person[k]=words[i]
         		
         		k=k+1
        	 	break
       		j=j+1
    		print i   
    		i=i+1


	i=0
	k=0

	while(i<len(words)):
    		j=0
    	while(j<len(obj)):
       
       		if(words[i]==per[j]):
         
         		vas[k]=words[i]
         		
         		k=k+1
        	 	break
       		j=j+1
    		print i   
    		i=i+1



        i=0
        n=0
        while(n<len(person))
	   while(i<len(pl)):
		if(place[n]==pl[i] and place[0]!=''):
		   pub.publish(str(po[n]))
                if(person[n]==per[i] and person[0]!=''):
                   pub1.publish(str(person[n]))
                if(vas[n]==obj[i]):
                   pub2.publish(str(vas[n]))
                i=i+1
           n=n+1'''

           
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
