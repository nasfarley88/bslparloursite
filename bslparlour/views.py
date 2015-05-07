from bslparlour.models import SourceVideo, NotSourceVideo
from bslparlour.serializers import SourceVideoSerializer, NotSourceVideoSerializer
from rest_framework import generics

# from .models import BSLDictionaryEntry, EnglishDictionaryEntry
# Create your views here.

# def index(request):
#     return HttpResponse("This is the index page.")


class SourceVideoList(generics.ListCreateAPIView):
    queryset = SourceVideo.objects.all()
    serializer_class = SourceVideoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NotSourceVideoList(generics.ListCreateAPIView):
    queryset = NotSourceVideo.objects.all()
    serializer_class = NotSourceVideoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
