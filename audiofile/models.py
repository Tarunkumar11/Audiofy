from django.db import models
from account.models import User
from django.utils import timezone

class Song(models.Model):
    song_name = models.CharField(verbose_name="Song name", max_length=100,blank=False,null=False)
    duration = models.PositiveIntegerField(verbose_name="Song's duration",blank=False,null=False)
    uploaded_time = models.DateField(verbose_name='uploaded_time', blank=False, null=False,default=timezone.now())

class Podcast(models.Model):
    name = models.CharField(verbose_name="Podcast name", max_length=100,blank=False,null=False)
    duration = models.PositiveIntegerField(verbose_name="Podcast duration",blank=False,null=False)
    uploaded_time = models.DateField(verbose_name='Uploaded time', blank=False, null=False,default=timezone.now())
    host = models.ForeignKey(User,verbose_name="Host name",on_delete=models.CASCADE,related_name="podcast_host")
    participants  = models.ManyToManyField(User,verbose_name="Participant names",null=True)

class Audiobook(models.Model):
    title  = models.CharField(verbose_name="Book title", max_length=100,blank=False,null=False,)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Author")
    narrator = models.ForeignKey(User,on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(verbose_name="Audio Book duration",blank=False,null=False)
    uploaded_time = models.DateField(verbose_name='uploaded_time', blank=False, null=False,default=timezone.now())
