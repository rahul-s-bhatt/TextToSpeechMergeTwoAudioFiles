from pydub import AudioSegment
import pyttsx3  

# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  
text = ""

with open('hyperbolic.txt', 'r') as reader:
	text += reader.read()

print(text)

# get details of speaking rate  
rate = engine.getProperty("rate")  
  
# setting new voice rate (faster)  
engine.setProperty("rate", 300)  
# engine.say(text)  
# engine.runAndWait() 
engine.setProperty('volume',0.5)
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.save_to_file(text, 'test.wav')
engine.runAndWait()

sound2 = AudioSegment.from_file('test.wav', format="wav")
sound1 = AudioSegment.from_file('lofi1.mp3', format="mp3")

louder = sound1 + 6

overlay = sound1.overlay(sound2, position = 0)

file_handle = overlay.export("output.mp3", format="mp3")
