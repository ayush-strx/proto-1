import asyncio
import edge_tts
from playsound import playsound
import uuid
import os

async def speak_async(text):
    voice = "en-US-GuyNeural"
    filename = f"output_{uuid.uuid4().hex}.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)
    try:
        playsound(filename)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def speak(text):
    asyncio.run(speak_async(text))