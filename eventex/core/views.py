# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk

def homepage(request):
    return render(request, 'index.html')


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)

def speaker_list(request):
    speakers = Speaker.objects.all()
    context = {'speakers': speakers}
    return render(request, 'core/speaker_list.html', context)

def talk_detail(request, pk):
    """
     Código refatorado, foi criado as properties:
       videos e slides na model Talk,
       assim enviando talk no context, automaticamente
       terá videos e slides
    """     
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,          
        #'slides': talk.media_set.filter(kind='SL'),
        #'videos': talk.media_set.filter(kind='YT'),
    }
    return render(request, 'core/talk_detail.html', context)

def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk_list.html', context)
