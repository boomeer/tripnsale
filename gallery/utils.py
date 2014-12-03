from gallery.models import *


def CreateGallery():
    g = Gallery()
    g.save(force_insert=True)
    return g


def CreateGalleryPhoto(gallery):
    photo = Photo(
        gallery=gallery,
    )
    photo.save(force_insert=True)
    return photo
