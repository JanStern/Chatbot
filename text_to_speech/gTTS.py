from gtts import gTTS
import os


def say_text(txt, lang: str = 'en'):
    tts_obj = gTTS(text=txt, lang=lang)
    tts_obj.save("example.mp3")
    os.system("mpg321 example.mp3")
    os.remove("example.mp3")


# say_text("Hello my friend. PUSSY")
