import pyaudio
import wave
import keyboard
import speech_recognition as sr


class STT:
# Records audio 
    def record_audio(filename): 
        chunk = 1024
        format = pyaudio.paInt16
        channels = 1 
        sample_rate = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

        print("Press and Hold the Shift Key to Record...")
        frames=[]

        keyboard.wait('shift')

        print("Recording...")

        while keyboard.is_pressed('shift'):
            data = stream.read(chunk)
            frames.append(data)

        print("Shift was Released...Stopped Recording.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

    # converts the audio
    def convert_wave_to_text(output_file, text_file="speech_to_text.txt"): 
        recognizer = sr.Recognizer()

        with sr.AudioFile(output_file) as source: 
            audio_data = recognizer.record(source)

            try: 
                text = recognizer.recognize_google(audio_data)
                with open(text_file, "w") as txt_file:
                    txt_file.write(text)
                print("Conversion saved to a text file")
            except sr.UnknownValueError: 
                print("Speech Recognition could not understand audio")
                return None
            except sr.RequestError as e: 
                print(f"Could not request results from google speech recognition service, {e}")
                return None
        
if __name__ == "__main__":
    output_file = "input.wav"

    STT.record_audio(output_file)

    result_txt = STT.convert_wave_to_text(output_file, text_file="speech_to_text.txt")

    if result_txt: 
        print("Text from audio:\n", result_txt)
    else: 
        print("Failed to convert audio to text")