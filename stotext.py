import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


with sr.AudioFile('C:\\Users\\hp\\Downloads\\NY045.wav') as source:
    audio = r.listen(source)

try:

    MyText = r.recognize_google(audio)
    MyText = MyText.lower()
    print(MyText)

    with open('C:\\Users\\hp\\Downloads\\myfile.txt', 'w') as w:
        w.write(MyText)
    # SpeakText(MyText)

except sr.RequestError as e:
    # print("Could not request results; {0}".format(e))
    pass

except sr.UnknownValueError:
    # print("unknown error occured")
    pass
