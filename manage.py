#!/usr/bin/env python
import os
import sys

import re

from bslparlour.models import SourceVideo
from bsldictionary.models import BSLEntry
from django.db import IntegrityError

def fill_bsl_entry(source_video=None, gloss=None, gloss_index=1, source_video_sha224=None):
    if source_video_sha224==None:
        source_video_sha224 = source_video.sha224
    print "source video sha224 fetched: " + source_video_sha224

    # If the video already has a gloss, don't bother with the function
    if len(BSLEntry.objects.filter(source_video_sha224=source_video_sha224))>0:
        print "Returning as " + source_video.filename + " already has an entry."
        return

    if source_video==None and (gloss==None or source_video_sha224==None):
        assert False, "Check your arguments!"
        
    if gloss==None:
        gloss = re.sub(r'(.MOV)|(.MP4)|(\(.*\))', '', source_video.filename.upper()).strip()
        gloss = gloss.replace('_', ' ')
        gloss = gloss.replace(' ', '-')
        gloss = gloss.strip()
    print "gloss generated: " + gloss
    print "gloss_index 'generated': " + str(gloss_index)
    

    try:
        BSLEntry.objects.create(
            gloss=gloss,
            gloss_index=gloss_index,
            source_video_sha224=source_video_sha224)
    except IntegrityError:
        gloss_index += 1
        fill_bsl_entry(gloss=gloss,
                       gloss_index=gloss_index,
                       source_video_sha224=source_video_sha224)
        

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bslparloursite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
