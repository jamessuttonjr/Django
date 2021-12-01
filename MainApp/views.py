from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics':topics}   
# the key is the variable used in the template file or the html file and the value of the dictionary is the variable used in the view function. WILL BE A QUESTION ON INTERVIEW
    
    return render(request, 'MainApp/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()

    context = context = {'topic':topic, 'entries':entries} 

    return render(request, 'MainApp/topic.html', context)