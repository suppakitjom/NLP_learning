import azure.cognitiveservices.speech as speechsdk
import time
from textToSpeech import speakText
from dialogflow import detect_intent

speech_config = speechsdk.SpeechConfig(
    subscription='44d7d58744334bea8b7c72de640ed3e3', region='southeastasia')
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
            print("RECOGNIZED KEYWORD: {}".format(evt.result.text))
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(exit_callback)
    speech_recognizer.start_keyword_recognition(model)
    print('---START---\n')

    while not done:
        time.sleep(.5)

    speech_recognizer.stop_keyword_recognition()

    print('Go ahead, say something')
    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Result: {}".format(result.text))
    return result.text


speakText(detect_intent(text='Sum of 5 and 8'))
