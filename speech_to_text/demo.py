import speech_recognition as sr
from typing import Text


def from_audio(audio_file) -> Text:
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    return r.recognize_google(audio)


def from_microphone(
        calibrate: bool = False
) -> Text:
    r = sr.Recognizer()
    s = sr.Microphone()
    with s as source:

        # only do it at the start. Takes up extra time
        if calibrate:
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

        print("Recording...")
        audio = r.record(source)
        print("Finished listening")
        return r.recognize_google(audio)

print(from_microphone())
