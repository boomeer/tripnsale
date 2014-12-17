from gallery.models import *
from util.utils import GetNewId
from PIL import Image
import os
from django.core.files import File


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


def StoreImage(image, field, sizeLimit=4*2**20):
    imageFileExt = os.path.splitext(image.name)[1]
    if imageFileExt not in [".jpg", ".jpeg", ".gif", ".png"]:
        raise Exception("bad_format")
    if image.size > sizeLimit:
        raise Exception("big_size")
    filePath = GetNewId() + imageFileExt
    field.save(filePath, image)
    return filePath

def MakeThumbnail(imgField, field):
    thumbTempPath = "/tmp/" + GetNewId() + ".jpg"
    im = Image.open(imgField.path)
    im.thumbnail((128, 128,))
    im.save(thumbTempPath, "JPEG")
    with open(thumbTempPath, "rb") as f:
        ff = File(f)
        StoreImage(ff, field)
