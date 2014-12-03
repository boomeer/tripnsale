from django.db import models
from django.contrib import admin


class Gallery(models.Model):
    def add(self, photo):
        photo.gallery = self
        photo.save()

    def getList(self):
        res = list(self.photo_set())
        return res

    def __str__(self):
        return str(id)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id",)


class Photo(models.Model):
    img = models.ImageField(upload_to="gallery_img", blank=True, null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, related_name="photos")

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("img", "gallery",)
