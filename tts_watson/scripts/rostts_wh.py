#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String
from tts_watson.TtsWatson import TtsWatson
import anyconfig
import bunch
import watson_developer_cloud
# Set up Assistant service.
service = watson_developer_cloud.AssistantV1(
  username = '0476d290-c1f9-4e14-9ea2-678a8dfede8a', # replace with service username
  password = '6676J281gkTK', # replace with service password
  version = '2018-07-10'
)
workspace_id = '5949c8af-9112-4452-884b-8efdcf692f4e' # replace with workspace ID

# Initialize with empty value to start the conversation.
global user_input
user_input = ''
global context
context = {}

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
          global user_input
          global context
          print(data.data)
          #if(pre!=data.data):
          i=0
          while True:
              i=i+1
              if i>5:
                 break

          # Send message to Assistant service.
              user_input = data.data
              response = service.message(
              workspace_id = workspace_id,
              input = {
                    'text': user_input
                     },
                     context = context
                    )
              
             # If an intent was detected, print it to the console.
              if response.result['intents']:
                 print('Detected intent: #' + response.result['intents'][0]['intent'])
          # Print the output from dialog, if any. Assumes a single text response.
              if response.result['output']['text']:
                 print(response.result['output']['text'][0])
                 self.ttsWatson.play(response.result['output']['text'][0])
                 break
          # Update the stored context with the latest received from the dialog.
              context = response.result['context']
              

          # Prompt for next round of input.
              
	    #self.ttsWatson.play('hello')
              #if(response.result['output']['text'][0]):
                
          #while(1):
          #     k=1
          
        

def listen():
    ttsWatsonRos = TtsWatsonRos()
    rospy.init_node('tts', anonymous=True)
    rospy.Subscriber("/decoded_msg", String, ttsWatsonRos.playSound )
    pub1 = rospy.Publisher('akh', String, queue_size = 10)
    print ('Ready to transform text into sound')
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listen()
