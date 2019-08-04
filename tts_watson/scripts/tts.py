#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String
from tts_watson.TtsWatson import TtsWatson
import anyconfig
import bunch


class TtsWatsonRos:
    CONFIG_FILE = "config1.yml"

    def __init__(self):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        configFile = currentDir + "/../" + self.CONFIG_FILE
        conf = anyconfig.load(configFile)
        bconf = bunch.bunchify(conf)
        self.ttsWatson = TtsWatson(bconf.user, bconf.password, bconf.voice, bconf.url, bconf.chunk)

    def playSound(self, data):
        print("hi")
	#self.ttsWatson.play('hello')
        self.ttsWatson.play(data.data)


def listen():
    ttsWatsonRos = TtsWatsonRos()
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("text_to_speech", String, ttsWatsonRos.playSound)
    print 'Ready to transform text into sound'
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listen()
