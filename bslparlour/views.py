from django.shortcuts import render
from django.http import HttpResponse

# from .models import BSLDictionaryEntry, EnglishDictionaryEntry
# Create your views here.

def index(request):
    return HttpResponse("This is the index page.")

# def gloss(request, gloss_str):
#     bsl_dict_entry_list = BSLDictionaryEntry.objects.all().filter(gloss=gloss_str.lower())
#     context = {
#         'bsl_dict_entry_list': bsl_dict_entry_list,
#     }
#     return render(request, 'bslparlour/gloss.html', context)

# def english(request, word_str):
#     english_dict_entry_list = EnglishDictionaryEntry.objects.all().filter(word=word_str.lower())
#     context = {
#         'english_dict_entry_list': english_dict_entry_list,
#     }
#     return render(request, 'bslparlour/english.html', context)
