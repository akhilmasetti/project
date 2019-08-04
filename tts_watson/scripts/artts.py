#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String
from tts_watson.TtsWatson import TtsWatson
import anyconfig
import bunch


class TtsWatsonRos:
    CONFIG_FILE = "config1.yml"
    global pre
    pre =1

    def __init__(self):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        configFile = currentDir + "/../" + self.CONFIG_FILE
        conf = anyconfig.load(configFile)
        bconf = bunch.bunchify(conf)
        self.ttsWatson = TtsWatson(bconf.user, bconf.password, bconf.voice, bconf.url, bconf.chunk)

    def playSound(self, data):
          print("hi")
          #if(pre!=data.data):
	    #self.ttsWatson.play('hello')
          self.ttsWatson.play(data.data)
          #while(1):
          #     k=1
          
        

def listen():
    ttsWatsonRos = TtsWatsonRos()
    rospy.init_node('tts', anonymous=True)
    rospy.Subscriber("response", String, ttsWatsonRos.playSound )
    pub1 = rospy.Publisher('akh', String, queue_size = 10)
    print ('Ready to transform text into sound')
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listen()
