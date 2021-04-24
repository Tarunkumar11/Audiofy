from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import UserSerializer
from django.http import Http404
from account.models import User
from rest_framework import generics

class UserCreate(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if not pk is None:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
        else:
            Songs = User.objects.all()
            serializer = UserSerializer(Songs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def post(self, request):
        password = request.data['password']
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user  = User(name=request.data['name'],username=request.data['username'],email=request.data['email'],password=password)
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    


        