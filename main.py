from model import Model
from speech_to_text import STT
from text_to_speech import TTS

stop_commands = ["Stop", "stop", "cease", "Cease"]

def main():
    text = record_audio()
    while text not in stop_commands:
        if text not in stop_commands:
            response = Model.final_result(text)
            result = response["result"]
            print(result)
            TTS.text_to_speech(result)
            TTS.play_audio()
        else:
            print("Stopping...")
        TTS.text_to_speech("Please ask your next question")
        TTS.play_audio()
        text = record_audio()
    TTS.text_to_speech("stopping program")
    TTS.play_audio()
    print("Stopping...")

def record_audio():
    output_file = "input.wav"
    STT.record_audio(output_file)
    result_txt = STT.convert_wave_to_text(output_file, text_file="speech_to_text.txt")
    if result_txt: 
        print("Text from audio:\n", result_txt)
    else: 
        print("Failed to convert audio to text")
    data = open("speech_to_text.txt", "r")
    text = data.read()
    return text

main()