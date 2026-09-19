import asyncio
import edge_tts
import pygame
from io import BytesIO

VOICE = "hi-IN-SwaraNeural"
RATE = "+25%"

pygame.mixer.init()


async def generate_audio(text):
    audio_buffer = BytesIO()
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])

    audio_buffer.seek(0)
    return audio_buffer


def speak(text):
    if not text or not text.strip():
        return

    text = text.replace(",", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    text = text.replace("--", " ")
    text = text.replace("—", " ")
    text = text.replace("...", ".")

    try:
        audio_buffer = asyncio.run(generate_audio(text))
        pygame.mixer.music.load(audio_buffer, "mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"[TTS Error]: {e}")