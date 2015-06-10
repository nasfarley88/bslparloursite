from django.db import models
from django.utils import timezone
from model_utils.fields import MonitorField
from sizefield.models import FileSizeField
from django.utils.html import format_html

class CastMember(models.Model):
    """Simple model to store basic information about people participating in videos."""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_names = models.CharField(max_length=120, blank=True)
    preffered_name = models.CharField(max_length=40, blank=True)
    bio = models.TextField()
    bio_last_update = MonitorField(monitor='bio')
    mug_shot = models.ImageField(blank=True) # TODO get a blank image to put here.

    def __unicode__(self):
        return self.first_name +" "+ self.last_name
    
# Create your models here.
class Video(models.Model):
    sha224 = models.CharField(max_length=56)
    filename = models.CharField(max_length=200)
    dropbox_directory = models.CharField(max_length=200)
    mime_type = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    size = FileSizeField()
    cast_members = models.ManyToManyField(CastMember)
    # owner = models.ForeignKey('auth.User', related_name='videos')

    def __unicode__(self):
        return self.filename or self.sha224_id


class SourceVideo(Video):
    vimeo_uri = models.IntegerField()
    # TODO replace with YouTube's equivilent of a URI
    youtube_url = models.CharField(max_length=140, blank=True)

    def vimeo_embed_property(self):
        return format_html('<iframe src="https://player.vimeo.com/video/'+str(self.vimeo_uri)+'?color=ffffff&title=0&byline=0&portrait=0" width="300" height="170" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>')
    vimeo_embed_property.allow_tags = True
    vimeo_embed = property(vimeo_embed_property)

    def __unicode__(self):
        return self.filename + " (" + str(self.vimeo_uri) +")" or self.sha224_id

class NotSourceVideo(Video):
    target_platform_choices = (
        ('twitter', 'Twitter'),
        ('tumblr', 'Tumblr'),
        ('facebook', 'Facebook'),
    )
    source_video = models.ForeignKey(SourceVideo)
    target_platform = models.CharField(max_length=10, choices=target_platform_choices)
    has_logo = models.BooleanField()

# class YouTubeVideo(models.Model):
#     source_video = models.ForeignKey(SourceVideo, db_column="sha224_id")
#     url = models.URLField()

# class BSLDictionaryEntry(models.Model):
#     source_videos = models.ManyToManyField(SourceVideo, db_column="sha224_id", related_name="source_videos")
#     preferred_source_video = models.ForeignKey(SourceVideo, db_column="sha224_id", related_name="preffered_source_video")
#     gloss = models.CharField(max_length=30)
#     example_glossed_phrase = models.CharField('A simple glossed phrased to indicate the approximate meaning of the sign', max_length=200, blank=True)
#     sign_descriptor = models.CharField(max_length=200, blank=True)

#     def __unicode__(self):
#         return self.gloss.upper()

# class EnglishDictionaryEntry(models.Model):
#     word = models.CharField(max_length=200)
#     definition_number = models.IntegerField()
#     definition = models.TextField()
#     bsl_dictionary_entry = models.ManyToManyField(BSLDictionaryEntry, blank=True)

#     def __unicode__(self):
#         return self.word.title()+" "+str(self.definition_number)+": "+\
#             self.definition[:40]+"..."

