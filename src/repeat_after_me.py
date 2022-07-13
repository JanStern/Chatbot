from speech_to_text.demo import from_microphone
from text_to_speech.gTTS import say_text

for i in range(5):

    text = from_microphone()
    say_text(text)
