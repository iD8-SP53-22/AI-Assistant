from model import Model
from speech_to_text import STT

stop_commands = ["Stop", "stop", "cease", "Cease"]

def main():
    text = record_audio()
    while text not in stop_commands:
        if text not in stop_commands:
            response = Model.final_result(text)
            print(response["result"])
        else:
            print("Stopping...")
        text = record_audio()
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