from django.contrib import admin
from bsldictionary.models import BSLEntry

from .models import (SourceVideo,
                     NotSourceVideo,
                     # YouTubeVideo,
                     # BSLDictionaryEntry,
                     # EnglishDictionaryEntry,
                     CastMember,
                     )

# class BSLDictionaryEntryAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('gloss',
#                        'source_videos',
#                        'preferred_source_video',
#                        'example_glossed_phrase',
#                        'sign_descriptor')
#         }),
#     )
#     filter_horizontal = ('source_videos',)

# class EnglishDictionaryEntryAdmin(admin.ModelAdmin):
#     filter_horizontal = ('bsl_dictionary_entry',)
# Register your models here.

class SourceVideoAdmin(admin.ModelAdmin):
    list_display = ('filename', 'vimeo_embed')
    list_per_page = 20
    search_fields = ('filename', )

admin.site.register(CastMember)
admin.site.register(SourceVideo, SourceVideoAdmin)
admin.site.register(NotSourceVideo)
# admin.site.register(YouTubeVideo)
# admin.site.register(BSLDictionaryEntry, BSLDictionaryEntryAdmin)
# admin.site.register(EnglishDictionaryEntry, EnglishDictionaryEntryAdmin)

