from django.db import models
from django.contrib import admin
import tripnsale.settings as settings


class Gallery(models.Model):
    head = models.ForeignKey("Photo", blank=True, null=True, related_name="heads")
    
    def add(self, photo):
        photo.gallery = self
        photo.save()

    def getList(self):
        res = list(self.photo_set())
        return res

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

