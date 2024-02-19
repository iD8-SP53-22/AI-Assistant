from openai import OpenAI

class Model:
    def run_model(client, history, prompt):
        # Initialize the pygame mixer
        # pygame.mixer.init()
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
            # Stop any currently playing music to release the file
            # pygame.mixer.music.stop()
            
            # Save the response to a file, clearing the file before writing
            with open('ai_responses.txt', 'w') as file:
                file.write(new_message["content"] + "\n")

            # Play the generated speech using pygame mixer
            # pygame.mixer.music.load("ai_response.mp3")
            # pygame.mixer.music.play()

            # Wait for the speech to finish playing
            # while pygame.mixer.music.get_busy():
            #     pygame.time.Clock().tick(10)

            history.append(new_message)
            
            # user_input = input("> ")
            history.append({"role": "user", "content": prompt})
            return new_message["content"]