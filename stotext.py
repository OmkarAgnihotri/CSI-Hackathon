import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def func(filename):
	with sr.AudioFile(filename) as source:
		audio = r.listen(source)

	try:
		MyText = r.recognize_google(audio)
		MyText = MyText.lower()
		print(MyText)

		with open('C:\\Users\\hp\\Downloads\\myfile.txt', 'w') as w:
			w.write(MyText)

	except sr.RequestError as e:
		pass

	except sr.UnknownValueError:
		pass

func('C:\\Users\\hp\\Downloads\\NY045.wav')

