#!/usr/bin/python2.7

import socket
import sys
import rospy
from std_msgs.msg import String

def speak_callback(data):

    host = rospy.get_param("~host", "192.168.43.121")
    port = int(rospy.get_param("~port", 8051))

    s = None
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print 'could not open socket'
        sys.exit(1)
    s.sendall(str(data.data))
    s.close()

#Subscriber
speak_sub = rospy.Subscriber('/speak', String, speak_callback)

if __name__ == '__main__':
    rospy.init_node('android_speech_synthesis_node')
    rospy.loginfo("android_speech_synthesis_node initialized")

    rospy.spin()
