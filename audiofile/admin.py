from django.contrib import admin
from .models import Song, Podcast, Audiobook
# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'duration', 'uploaded_time')
    readonly_fields = ['uploaded_time']
    search_fields = ['song_name']

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'uploaded_time','host')
    readonly_fields = ['uploaded_time']
    search_fields = ['name']

class AudiobookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author','narrator', 'duration', 'uploaded_time')
    readonly_fields = ['uploaded_time']
    search_fields = ['title']
    list_filter = ['author','narrator']


admin.site.register(Song,SongAdmin)
admin.site.register(Podcast,PodcastAdmin)
admin.site.register(Audiobook,AudiobookAdmin)


