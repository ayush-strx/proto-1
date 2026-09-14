import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except:
        print("Could not understand")
        return ""