import pyttsx3
engine=pyttsx3.init()
engine.say("a a k k alias anil kumar")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.say("turn left````")
engine.runAndWait()