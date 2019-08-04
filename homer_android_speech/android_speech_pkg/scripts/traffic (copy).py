#!/usr/bin/python2.7

import rospy
from std_msgs.msg import String
global akhil
global n
n=0


def traffic():
        global pub
        global pub1
        global akhil
        global n 
        global pub2
        global pub5
        global pub4
        global pub10
        sen=akhil
        ss="my task is "+sen
        ss1="Hi nikhil. Hello nikhil. senseless nikhil "
        pub5.publish(ss)
        pub5.publish(ss1)
	v=['GET','GRASP','TAKE','PICK','DELIVER','PUT','PLACE','TELL','SAY','GO','NAVIGATE','ENTER','FIND']
	pl=['EXIT','TABLE','COUNTER','KITCHEN','BEDROOM','LIVING','CORRIDOR','OFFICE','DINNING','BAR','SINK','','']
	obj=['BOTTLE','BOWL','LAPTOP','CHAIR','COKE','TEA','BEER','BISCUITS','SOAP','LAPTOP','','','']
	id1=['','45','63','63','','','','','','','','','']
        per=['','NIKHIL','AKHIL','TAMMANA','','','','','','','','','']
	po =['','6.728 0.024++','5.846 3.647+-','','4.150 3.339+-','','','','','','','','']
        
        i=0
               
	j=0
	k=0
	verbs=['','','','','','']
	place=['','','','','','']
	person=['','','','','','']
	vas=['','','']
        words = akhil.split()
	print len(words)
	while(i<len(words)):
   	    j=0
    	    while(j<len(v)):
       
        	if(words[i]==v[j]):
         
         		verbs[k]=v[j]
         		
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
         
         		place[k]=pl[j]
         		
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
         
         		person[k]=per[j]
         		
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
         
         		vas[k]=words[i]
         		
         		k=k+1
        	 	break
       		j=j+1
    		print i   
    	   i=i+1

        print vas

        


        i=0
        
        print person
	while(i<len(pl)):
          if(verbs[n]==v[i] and verbs[n]!=''):
             if(v[i]=='PICK'):
               asdf=1
               #pub10.publish(id1[i])
	  elif(place[n]==pl[i] and place[n]!=''):
	     pub.publish(str(po[i]))
          elif(person[n]==per[i] and person[n]!=''):
             pub2.publish(str(person[n]))
             
          elif(vas[n]==obj[i] and vas[n]!=''):
            # pub1= rospy.Publisher('/object', String, queue_size=10)
             print "hello"
             ak='hello'
             if(verbs[n]=="PICK"):
               pub10.publish(id1[i])
             else:
               pub1.publish(obj[i])
          print vas[n]==obj[i] and vas[n]!=''
          i=i+1
        
        
        i=0
        while(i<len(words)):
           if(words=="ASK"):
             aa="ok"
             pub4.publish(aa)


def traff(data):
    global n
    print "hiii"
    n=n+1
    traffic()
    
def akhil(data):
    global akhil
    akhil=data.data
    traffic()
    
    




def listener():
    global pub
    global pub1
    global pub2
    global pub5
    global pub4
    global pub10
    rospy.init_node('traffic1',anonymous=True)
    pub5 = rospy.Publisher('/recognized_speech', String, queue_size=10)
    rospy.Subscriber('/traff',String,traff)
    rospy.Subscriber('/akhil',String,akhil)
    pub = rospy.Publisher('/posision', String, queue_size=10)
    pub1= rospy.Publisher('/object', String, queue_size=10)
    pub2 = rospy.Publisher('/person',String, queue_size=10)
    pub4 = rospy.Publisher('/que',String,queue_size=10)
    pub10=rospy.Publisher('/obj_id',String,queue_size=10)
    rospy.spin()
    
    
    
    




if __name__=='__main__':
   listener()

