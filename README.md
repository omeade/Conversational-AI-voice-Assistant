Overview:
A Python-based voice assistant that provides a conversational AI experience through voice commands. 
The system listens to your speech, processes it through AI, and responds back audibly, creating a hands-free interactive assistant.
Overview
Jarvis is a local voice assistant built with Python that combines speech recognition, natural language processing, 
and text-to-speech synthesis. It creates a continuous conversation loop where you can speak naturally and receive intelligent responses.
The assistant uses Voice Activity Detection (VAD) to automatically detect when you start and stop speaking, 
eliminating the need for push-to-talk buttons or wake words. Once it is activated, it transcribes your speech using the Whisper model, sends the text to a local Ollama AI model for processing, 
and says the response back to you using text-to-speech.

I created this project off inspiration from Jarvis in the Avengers movies. I thought it would be a cool project that I could work on and challange myself in.

Current problems im having:
Finding a system requirments medium to allow this to work on systems of multiple CPU/GPU power.

What i'm working on:
Creating AI fallbacks if Ollama fails.
Getting the correct version of the Whisper Model to detect and script the voice of the person speaking at all times and error free.

