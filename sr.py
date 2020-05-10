import speech_recognition as sr
r=sr.Recognizer()
print(sr.Microphone)

with sr.Microphone() as source:
    print("speak anything")
    audio=r.listen(source)
    print(audio)
    try:
        text=r.recognize_google(audio)
        print("you said {}".format(text))
    except:
        print("onum purila")