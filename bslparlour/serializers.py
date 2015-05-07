from django.forms import widgets
from rest_framework import serializers, permissions
from bslparlour.models import SourceVideo, NotSourceVideo, CastMember

class SourceVideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = SourceVideo
        fields = ('sha224_id',
                  'filename',
                  'dropbox_directory',
                  'mime_type',
                  'size',
                  'vimeo_uri',
                  'youtube_url',
                  'owner')

class NotSourceVideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = NotSourceVideo
        fields = ('sha224_id',
                  'filename',
                  'dropbox_directory',
                  'mime_type',
                  'size',
                  'source_video',
                  'target_platform',
                  'has_logo',
                  'owner')
