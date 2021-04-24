from audiofile.models import Song, Podcast, Audiobook
from rest_framework import serializers
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name","email", "username",'password']
        extra_kwargs = {'password': {'write_only': True}}
