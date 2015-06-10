from django.shortcuts import render
from bsldictionary.models import BSLEntry

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, 'bslgames/index.html', {})

def name_that_sign(request):
    choice = random.choice(BSLEntry.objects.filter(level='basic'))
    choice_video = choice.source_videos.all().order_by('-date_added')[0]
    context = { 'choice': choice, 'choice_video': choice_video, 'choice_gloss_lower': choice.gloss.lower() }
    return render(request, 'bslgames/name_that_sign.html', context)
