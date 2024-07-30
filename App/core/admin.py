from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):

    list_display = ('id',)
    list_filter = ('id',)
    search_fields = ('id',)


admin.site.register(Image, ImageAdmin)

