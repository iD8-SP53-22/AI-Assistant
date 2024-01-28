from gtts import gTTS
from playsound import playsound
import os
text = "hiiiiiiii"

class TTS: 
    def text_to_speech(text):
        message = text
        speech = gTTS(text = message)
        speech.save("audio.mp3")
    
    def play_audio():
        playsound("audio.mp3")
        os.remove("audio.mp3")


def tests():
    TTS.text_to_speech(text)
    TTS.play_audio()