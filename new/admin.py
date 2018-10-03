from django.contrib import admin
from .models import *
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name']
class AudioAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','audio']
    prepopulated_fields = {'slug': ['name']}
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['lastname']
    list_display = ['id','lastname','firstname','date_birtday','photo']
    prepopulated_fields = {'slug': ['lastname']}
class VideoAdmin(admin.ModelAdmin):
    search_fields =['name']
    list_display = ['name','video']
    prepopulated_fields = {'slug': ['name']}
class ImageAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','image']

admin.site.register(Genre,GenreAdmin)
admin.site.register(Audio,AudioAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Image,ImageAdmin)

# Register your models here.
