from django.contrib import admin

from .models import BSLDictionaryTweet

# Register your models here.

class BSLDictionaryTweetAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'bsl_entry')
    list_display_links = ('bsl_entry',)
    list_editable = ('tweet',)
    search_fields = ('tweet',)

    list_per_page = 20

admin.site.register(BSLDictionaryTweet, BSLDictionaryTweetAdmin)
