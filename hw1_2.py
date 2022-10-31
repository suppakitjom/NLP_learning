from wakeWordActivation import wakeWordActivation
from textToSpeech import speakText
from dialogFlow import detect_intent
import os

os.system('clear')
prompt = wakeWordActivation()
result = detect_intent(prompt)
print('>>>> {}'.format(result))
speakText(result)
