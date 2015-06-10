from django.contrib import admin
from .models import BSLEntry, EnglishEntry
# Register your models here.

class BSLEntryAdmin(admin.ModelAdmin):
    filter_horizontal = ('source_videos',)
    search_fields = ('gloss', 'level')
    list_display = ('gloss', 'level',)
    list_editable = ('level',)
    list_display_links = ('gloss',)
    


admin.site.register(BSLEntry, BSLEntryAdmin)
admin.site.register(EnglishEntry)
