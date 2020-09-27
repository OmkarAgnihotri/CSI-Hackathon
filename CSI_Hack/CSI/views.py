from django.shortcuts import render
from django.http import HttpResponse
from .models import AUDIO
from .forms import BasicForm
from CSI.tasks import speechToText

temp = [
	{
		'par':'Dharansh',
		'title':'CSI 1'
	},
	{
		'par':'Dharansh 1',
		'title':'CSI 2'
	}

]


def home(request): 

	if request.method == 'POST' :
		print(request.POST)
		print(request.FILES)
		name = request.POST['name']
		file = request.FILES['file']
		print(temp)
		print(request.POST)
		Student = AUDIO(name=name,file=file)
		Student.save()
		return HttpResponse("<h1> succeed </h1>")


	form = BasicForm()
	print(request.body)
	return render(request,'CSI/formss.html',{'form' : form})

def teacher(request):
	context = {
		'content' : AUDIO.objects.all()
	}
	return render(request,'CSI/teachers.html',context)

def speech_to_text(request):
	speechToText.delay()
	return render(request,'CSI/response.html')