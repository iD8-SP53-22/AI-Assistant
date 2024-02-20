from openai import OpenAI
from speech_to_text import STT
from text_to_speech import TTS

stop_commands = ["terminate", "Terminate"]
special_char = ["!","~","@","#","$","%","^","&","*","(",")","-","_","=","+",",","{","]","[","]","|",";",":","'","<",">","?","/","`",",","."]
nums = ["1","2","3","4","5","6","7","8","9","0"]
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
{"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
{"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

def main():
    text = " "
    while text not in stop_commands:
        if text not in stop_commands:
            completion = client.chat.completions.create(
                model="local-model",  # this field is currently unused
                messages=history,
                temperature=0.7,
                stream=True,
            )
            new_message = {"role": "assistant", "content": ""}

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    new_message["content"] += chunk.choices[0].delta.content                                                                                                                                        
            with open('ai_responses.txt', 'w') as file:
                file.write(new_message["content"] + "\n")
            history.append(new_message)
            # TTS.text_to_speech(new_message["content"])
            # TTS.play_audio()
            text = input(f"\n>")
            history.append({"role": "user", "content": text})
        else:
            print("Stopping...")
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

def validate_input():
    text = input(f"\n>")
    detector = 1
    while detector >= 1:
        detector = 1
        for i in range(0, len(text)):
            print(f"index: {i}")
            print(f" index : {i}, letter: {text[i]}")
            if text[i] in special_char or text[i] in nums:
                print(f"Unauthorized Characters detected, please enter a new prompt")
                detector = 1
                text = input(f"\n>")
            else:
                detector = 0
    return text

main()