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
