from django.db import models
from django.contrib import admin
import tripnsale.settings as settings
from datetime import datetime


class Gallery(models.Model):
    head = models.ForeignKey("Photo", blank=True, null=True, related_name="heads")
    createTime = models.DateTimeField(default=datetime.now())
    token = models.TextField(default="")
    
    def add(self, photo):
        photo.gallery = self
        photo.save()

    def getPhotos(self):
        photos = self.photos.filter(verified=True).all()
        return photos

    def __str__(self):
        return str(id)

    def getHeadUrl(self):
        return self.head.img.url if self.head else settings.STATIC_URL + "/no-photo.jpg"

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id",)


class Photo(models.Model):
    img = models.ImageField(upload_to="gallery_img", blank=True, null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, related_name="photos")
    thumbnail = models.ImageField(upload_to="gallery_img", blank=True, null=True)
    token = models.TextField(default="")
    verified = models.BooleanField(default=True)
    
    def thumbUrl(self):
        return self.thumbnail.url if self.thumbnail else ""

    def url(self):
        return self.img.url
