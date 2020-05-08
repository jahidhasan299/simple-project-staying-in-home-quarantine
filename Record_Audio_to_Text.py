import speech_recognition as sr
sr.__version__
r = sr.Recognizer()
with sr.AudioFile(output.mp3) as source:
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Converting Speach to text .....")
        print(text)
    except:
        print("Sorry Try again later")
