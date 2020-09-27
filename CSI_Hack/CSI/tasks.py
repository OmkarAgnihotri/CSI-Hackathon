from celery import shared_task
from .models import AUDIO
from .stotext import func

@shared_task
def speechToText():
    data = AUDIO.objects.all()

    transcript_files = []
    for row in data:
        # print(row.file)
        transcript_files.append(func(row.file))

    for i in range(len(data)):
        data[i].transcript = transcript_files[i]
        data[i].save()


    
