import azure.cognitiveservices.speech as speechsdk
import time
from textToSpeech import speakText
# .env reader
from dotenv import load_dotenv
import os

load_dotenv()

speech_config = speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"),
                                       region=os.getenv("SPEECH_REGION"))
speech_config.speech_recognition_language = "en-US"
speech_config.speech_recognition_language = "en-US"


def wakeWordActivation():
    #if wakeword is not string or empty, return
    model = speechsdk.KeywordRecognitionModel(
        "e907bd72-6dff-4316-bc33-1140bffc4686.table")
    # keyword = 'hey dude whats up'
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                   audio_config=audio_config)
    done = False

    def exit_callback(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedKeyword:
            print('>>>> Hi, how can I help you?')
            speakText('Hi, how can I help you?')
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(exit_callback)
    speech_recognizer.start_keyword_recognition(model)
    print('say \"hey dude whats up\" to activate\n')

    while not done:
        time.sleep(.5)

    speech_recognizer.stop_keyword_recognition()

    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("<<<< {}".format(result.text))
    return result.text