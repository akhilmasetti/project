# tts-watson-ros
Text to speech using watson for ros.

## Requirements

- **Python 2.7**
- **Pip**
- Ros indigo (maybe can be used on new version of ros but this is not tested)
- **portaudio**, can be installed with `brew install portaudio` (mac) or `apt-get install portaudio19-dev`(linux)

## Usage

1. Clone the repo ìn your catkin workspace (most of the time it's `~/catkin_ws`) `src` folder: `git clone https://github.com/HomeHabbit/tts-watson-ros.git tts_watson`
2. Do `catkin_make` under your catkin workspace
3. Run `pip install -r requirements.txt` inside `tts_watson` folder
4. Update the file `config.sample.yml` and rename it to `config.yml`
5. Run it with ros: `rosrun tts_watson tts.py`
6. You need to publish message on topic `/text_to_speech` (e.g with rostopic: `rostopic pub /text_to_speech std_msgs/String hi` will make you hear "hi")