from textToSpeech import speakText
from wakeWordActivation import wakeWordActivation
import os

os.system('clear')
prompt = wakeWordActivation()
print('>>>> {}'.format(prompt))
speakText(prompt)
