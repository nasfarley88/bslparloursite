from bslbot import myconf
import tweepy
import logging
import sys
import random
import datetime
import dropbox
import os

from .models import BSLDictionaryTweet
from bslparlour.models import SourceVideo, NotSourceVideo 
from bsldictionary.models import BSLEntry

def tweet_random_dict_entry():
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    tweepy_auth = tweepy.OAuthHandler(
        myconf.consumer_key,
        myconf.consumer_secret,
    )
    tweepy_auth.set_access_token(
        myconf.access_key,
        myconf.access_secret,
    )
    tweepy_api = tweepy.API(tweepy_auth)

    dbox_client = dropbox.client.DropboxClient(myconf.dbox_master_key)

    bsl_dictionary_tweet = random.choice(BSLDictionaryTweet.objects.all())

    bsl_entry = bsl_dictionary_tweet.bsl_entry

    source_video = SourceVideo.objects.get(sha224=bsl_entry.source_video_sha224)

    gif_record = NotSourceVideo.objects.get(source_video=source_video, target_platform='twitter')

    f, metadata = dbox_client.get_file_and_metadata(
        os.path.join(gif_record.dropbox_directory, gif_record.filename))
    out = open(gif_record.filename, 'wb')
    out.write(f.read())
    out.close()

    tweepy_api.update_with_media(gif_record.filename, status=bsl_dictionary_tweet.tweet)

    print bsl_dictionary_tweet.tweet, source_video    

if __name__ == '__main__':
    tweet_random_dict_entry()
