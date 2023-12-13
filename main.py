import speech_recognition as sr
import numpy as np

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

    try:
        
        audio_signal = np.frombuffer(audio.frame_data, dtype=np.int16)

        print("Audio Signal:", audio_signal)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error:", e)
