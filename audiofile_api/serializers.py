from audiofile.models import Song, Podcast, Audiobook
from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","email", "username","is_host"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['pk', 'song_name', 'duration','uploaded_time']
        read_only_fields = ['uploaded_time']
    

class PodcastSerializer(serializers.ModelSerializer):
    host = UserSerializer(serializers.RelatedField(source='User', read_only=True))
    participants  = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Podcast
        fields = ['pk', 'name', 'duration','uploaded_time','host','participants']
        read_only_fields = ['uploaded_time']
    
class PodcastSerializersave(serializers.ModelSerializer):
    #host = UserSerializer(serializers.RelatedField(source='User', read_only=True))
    participants  = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Podcast
        fields = ['pk', 'name', 'duration','uploaded_time','host','participants']
        read_only_fields = ['uploaded_time']


class AudiobookSerializersave(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,slug_field='username')
    narrator= serializers.SlugRelatedField(many=False, read_only=True,slug_field='username')
    class Meta:
        model = Audiobook
        fields = ['pk', 'title', 'author','narrator','duration','uploaded_time']
        read_only_fields = ['uploaded_time']

class AudiobookSerializerget(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    narrator= UserSerializer(read_only=True)
    class Meta:
        model = Audiobook
        fields = ['pk', 'title', 'author','narrator','duration','uploaded_time']
        read_only_fields = ['uploaded_time']


        
        