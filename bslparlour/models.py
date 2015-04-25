from django.db import models
from hashlib import sha224

class CastMember(models.Model):
    """Simple model to store basic information about people participating in videos."""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_names = models.CharField(max_length=120, blank=True)
    preffered_name = models.CharField(max_length=40, blank=True)
    bio = models.TextField()
    bio_last_update = models.DateTimeField()
    # mug_shot = models.ImageField()

    def __unicode__(self):
        return self.first_name +" "+ self.last_name

    

# Create your models here.
class Video(models.Model):
    # TODO figure out the real length that is needed for each field
    sha224_id = models.CharField(primary_key=True, max_length=56)
    filename = models.CharField(max_length=200)
    dropbox_directory = models.CharField(max_length=200)
    mime_type = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date added to database')
    size = models.BigIntegerField()
    cast_members = models.ManyToManyField(CastMember)
    
    def __unicode__(self):
        return self.filename or self.sha224_id


class SourceVideo(Video):
    vimeo_uri = models.IntegerField()
    # TODO replace with YouTube's equivilent of a URI
    youtube_url = models.CharField(max_length=140, blank=True)

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

