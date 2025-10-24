import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import pyttsx3
import ollama
import time
import os
import webrtcvad
import collections

whisper_model = WhisperModel("small", device="cpu")  
engine = pyttsx3.init()

def listenVad(max_time=10):
    

    print("🎤 Listening...")
    samplerate = 16000
    vad = webrtcvad.Vad(2)  
    frame_duration = 30 
    frame_size = int(samplerate * frame_duration / 1000)
    
    audio_buffer = []
    silence_frames = 0
    max_silence = int(500 / frame_duration)  
    
    start_time = time.time()
    while True:
        chunk = sd.rec(frame_size, samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        audio = np.array(chunk).tobytes()
        audio_buffer.append(chunk)
        is_speech = vad.is_speech(audio, samplerate)
        if not is_speech:
            silence_frames += 1
        else:
            silence_frames = 0
        if silence_frames > max_silence or (time.time() - start_time) > max_time:
            break
    audio_np = np.concatenate(audio_buffer)
    return np.squeeze(audio_np)


def listenAndTranscribe(max_time=10):

    audio = listenVad(max_time=max_time)
    audio = audio.astype(np.float32) / 32768.0   # convert to float32
    audio = audio / np.max(np.abs(audio)) 
    

    segments, _ = whisper_model.transcribe(audio)
    text = ''.join([s.text for s in segments]).strip()
    
    print("You said:", text)
    return text



def askAi(prompt):
    if not prompt.strip():
        return "I didn't catch that."
    try:
        response = ollama.generate(
            model="gemma:2b-instruct",
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error: {e}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Jarvis online. How can I help you, Odhran?")
    while True:
        query = listenAndTranscribe()  
        if not query:
            continue
        if any(word in query.lower() for word in ["stop", "exit", "goodbye"]):
            speak("Goodbye, Odhran.")
            break
        reply = askAi(query)
        print("...:", reply)
        speak(reply)
