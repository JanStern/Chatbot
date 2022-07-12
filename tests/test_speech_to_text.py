"""
Tests if Speech to Text works
"""
from speech_to_text.demo import from_audio
from os import path


class TestSpeechToText:

    def test_speech_to_text_from_audio(self):
        """
        Test if the speech recognizer works on the test-audio.flac
        """
        audio_file = path.join(path.dirname(path.realpath(__file__)), "../resources/test-audio.flac")
        text = from_audio(audio_file)
        assert text == "this is a test audio file"

    def test_EXAMPLE(self):
        assert 1 == 1
