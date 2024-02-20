from openai import OpenAI
from speech_to_text import STT
from text_to_speech import TTS

stop_commands = ["terminate", "Terminate"]
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
{"role": "system", "content": "You are an intelligent assistant that is being developed by Albert Alvaro and Namman Shukla, moreover you are honest and may not make things up, you must also always limit the characters of your responses to be under or equal to 100 characters, you also may not use emojis"},
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
            # Uncomment bellow Lines to use gTTs
            # TTS.text_to_speech(new_message["content"])
            # TTS.play_audio()

            #  Below is the code to use Elevenlabs, comment it out to use gTTS
            data = open("ai_responses.txt", "r")
            text = data.read()
            TTS.EL_TTS(text)

            text = input(f"\n>")
            history.append({"role": "user", "content": text})
        else:
            print("Stopping...")
    TTS.EL_TTS("Stopping Program")
    print("Stopping...")

#  Audio recording function that will return a str of the speech picked up by the microphone
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