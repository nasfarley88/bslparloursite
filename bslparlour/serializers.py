from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers, permissions
from bslparlour.models import SourceVideo, NotSourceVideo, CastMember

class SourceVideoSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = SourceVideo
        fields = ('sha224',
                  'filename',
                  'dropbox_directory',
                  'mime_type',
                  'size',
                  'vimeo_uri',
                  'youtube_url',
                  )

class NotSourceVideoSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = NotSourceVideo
        fields = ('sha224',
                  'filename',
                  'dropbox_directory',
                  'mime_type',
                  'size',
                  'source_video',
                  'target_platform',
                  'has_logo',
                  )

class UserSerializer(serializers.ModelSerializer):
    """Serializer for users. """

    source_videos = serializers.PrimaryKeyRelatedField(many=True, queryset=SourceVideo.objects.all())
    not_source_videos = serializers.PrimaryKeyRelatedField(many=True, queryset=NotSourceVideo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'source_videos', 'not_source_videos')
    
