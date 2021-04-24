from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from audiofile.models import Song, Podcast, Audiobook
from .serializers import SongSerializer,PodcastSerializerget,AudiobookSerializerget,UserSerializer,PodcastSerializersave,AudiobookSerializersave
from django.http import Http404
from account.models import User


class SongList(APIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404
    
    def get(self, request,pk=None):
        if not pk is None:
            Songs = self.get_object(pk)
            serializer = SongSerializer(Songs)
        else:
            Songs = Song.objects.all()
            serializer = SongSerializer(Songs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
        
    def put(self, request, pk=None, format=None):
        if pk is None:
            data =  {"info": "Please provide the ID of the song"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        OneSong = self.get_object(pk)
        serializer = SongSerializer(OneSong, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,pk=None):
        serializer = SongSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        OneSong = Song(song_name=request.data['song_name'],duration=request.data['duration'])
        OneSong.save()
        return Response(SongSerializer(OneSong).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None, format=None):
        song = self.get_object(pk)
        name = song.song_name
        song.delete()
        return Response( {"info": "{0} has been deleted successfully".format(name)},status=status.HTTP_200_OK)

class PodcastList(APIView):
    serializer_class = PodcastSerializersave
    queryset = Podcast.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Podcast.objects.get(pk=pk)
        except Podcast.DoesNotExist:
            raise Http404

    def get(self, request,pk=None):
        if not pk is  None:
            podcast = self.get_object(pk)
            serializer = PodcastSerializerget(podcast)
        else:
            podcast = Podcast.objects.all()
            serializer = PodcastSerializerget(podcast, many=True)
        return Response(serializer.data) 

    def put(self, request, pk=None, format=None):
        if pk is None:
            data =  {"info": "Please provide the ID of the song"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        Onepodcast = self.get_object(pk)
        serializer = PodcastSerializersave(Onepodcast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)
    
    def post(self,request,pk=None):
        if pk is not None:
            return Response({'Error':"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

        if len(request.data.get('participants'))>10:
            return Response({'Error':"Maximam 10 Participants can be added"}, status=status.HTTP_400_BAD_REQUEST)
        
        Not_exist_participant_name = self.check_participant(request.data['participants'])
        if len(Not_exist_participant_name) != 0:
            return Response({"Error":Not_exist_participant_name  + 'do not exist'},status=status.HTTP_403_FORBIDDEN)
        
        try:
            host = User.objects.get(username=request.data.get('host'))
        except:
            host = None
        if host is None:
            return Response({'Error':"Please provide correct host"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PodcastSerializersave(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        onepodcast = Podcast(name=request.data['name'],duration=request.data['duration'],host=host)
        onepodcast.save()
        for participant in request.data['participants']:
            obj  = User.objects.get(username=participant)
            onepodcast.participants.add(obj)
        onepodcast.save()
        return Response(PodcastSerializerget(Podcast.objects.get(pk=onepodcast.id)).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None, format=None):
        if pk is None:
            data =  {"info": "Please provide the ID of the Podcast"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        podcast = self.get_object(pk)
        name = podcast.name
        podcast.delete()
        messages = {'message':'{0} Podcast has been deleted'.format(name)}
        return Response(messages,status=status.HTTP_200_OK)

    def check_participant(self,participants):
        temp_participant = ''
        for participant in participants:
            try:
                obj  = User.objects.get(username=participant)
            except:
                temp_participant += participant + " "

        return temp_participant
                

class AudiobookList(APIView):
    serializer_class = AudiobookSerializersave
    queryset = Audiobook.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self, pk):
        try:
            return Audiobook.objects.get(pk=pk)
        except Audiobook.DoesNotExist:
            raise Http404

    def get(self, request,pk=None):
        if pk != None:
            audio_book = self.get_object(pk)
            serializer = AudiobookSerializerget(audio_book)
        else:
            audio_book = Audiobook.objects.all()
            serializer = AudiobookSerializerget(audio_book, many=True)
        return Response(serializer.data) 

    def put(self, request, pk=None, format=None):
        if pk is None:
            return Response({"message":"Please provide audiobook ID"})

        one_audio_book = self.get_object(pk)
        serializer = AudiobookSerializersave(one_audio_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,pk=None):
        serializer = AudiobookSerializersave(data=request.data)
        if  serializer.is_valid():
            print(serializer.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        author = User.objects.get(username=request.data['author'])
        narrator = User.objects.get(username=request.data['narrator'])
        audio_book = Audiobook(title=request.data['title'],author=author, narrator=narrator,duration=request.data['duration'])
        audio_book.save()
        return Response(AudiobookSerializerget(Audiobook.objects.get(pk=audio_book.id)).data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None, format=None):
        if pk is None:
            return Response({"message":"Please provide audiobook ID"})
        audio_book = self.get_object(pk)
        title = audio_book.title
        audio_book.delete()
        message = {'message':"{0} has been deleted".format(title)}
        return Response(message,status=status.HTTP_204_NO_CONTENT)