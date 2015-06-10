from django.db import models
from django import forms
from bsldictionary.models import BSLEntry

# Create your models here.
class Tweet(models.Model):
    """Base class for a tweet."""
    tweet = models.CharField(max_length=140)
    last_tweeted = models.DateTimeField(blank=True)

    def __unicode__(self):
        return self.tweet
        

class BSLDictionaryTweet(Tweet):
    """BSLDictionary entry tweet model."""
    bsl_entry = models.ForeignKey(BSLEntry)
