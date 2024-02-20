from gtts import gTTS
from elevenlabs import generate, play
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
    def EL_TTS(text):
        audio = generate(
            api_key="61d0f46b9dc99fce221ba868bfd63edf",
            text=text,
            voice="Rachel",
            model="eleven_multilingual_v2"
            )
        play(audio)


def tests():
    TTS.text_to_speech(text)
    TTS.play_audio()