// this file contain the pseudocode i plan to write down while making this project \\

using the lib called livewhisper (openai) gonna make a **live transcription program** that 
                will transcribe and clear out the file after a certain limit (like 4 lines) #NOTE: (23/01) Instead of live transcribing it since our computational power is not meeting the requirement, we can record the audio and then transcribe it. So the program records a .WAV file and transcribe it to text and then that text file can go to the LLM, generating a response.
                                    and 
                will follow command like words "hello <name>", "<name>", "stop" etc (havent decided yet lol)
the transcription will go to a text file. 

that text file will be read by a llm (llama 2) using a **LLM program** 
and will reply to it (still figuring this bit out) 

the reply given by llama 2 will also then be saved in a text file which will be read out by a **TTS program** attached to a model or image 

the realism will be head movement of the model/image


#TO-DO 
have to figure out a way to connect all the 3 programs together 
have to figure out how to use llama 

Albert Notes:

Manged to figure out how to use Llama2 also managed to connect the speech to text stuff with the model in the main.py file, everything has been tested and works pretty well, except for the fact that the model is truly shit, it works on and off, menaing that it can spew out answers but sometimes the answer comes out truly shit, also even with my hardware it is using up a metric ton of my cpu, almost 100% of it everytime a prompt is given, moreover for now only medical knowledge is present within the bot as I had not given it anything else. It is also extremely slow.

Here are the steps to actually activate everything.

1. Create a virtual environment through your terminal, a Python Venv is good enough, I dunno how to use Condaenv, even if it can make everything much more efficient
2. Within the directory pull the git branch 'main'
3. pip install the requirements.txt file through inputting 'pip install -r requirements.txt' in the terminal
4. Download the llama-2-7b-chat.ggmlv3.q8_0.bin file from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main and place it in the project directory
5. Create a data folder and insert the PDF file you want the AI to learn from, it must be in PDF and the folder must be named 'data'
6. Run the ingest.py file and wait a few minutes, a folder named vectorstores should have been created containing both the .pkl and .faiss files
7. After which directly run the main.py file and everything should run decently well

* P.S. If you run the main.py file ignore the warnings about langchain depreciating and asking you to install the community version, it is inconsequential.
* P.S.S. I ignored a lotta shit, don't pay too much attention to it, it's mostly things you gotta get yourself to make this work.
