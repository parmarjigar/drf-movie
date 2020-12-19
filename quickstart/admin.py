from django.contrib import admin

# Register your models here.
from .models import Cast, Media, MediaFile

admin.site.register(Cast)
admin.site.register(Media)
admin.site.register(MediaFile)
