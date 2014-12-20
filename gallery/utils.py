from gallery.models import *
from util.utils import GetNewId
from PIL import Image
import os
from django.core.files import File
from datetime import datetime


def CreateGallery():
    g = Gallery(
        createTime=datetime.now(),
        token=GetNewId(),
    )
    g.save(force_insert=True)
    return g


def CreateGalleryPhoto(gallery, token=None):
    if not token:
        token = GetNewId()
    photo = Photo(
        gallery=gallery,
        token=token,
        verified=False,
    )
    photo.save(force_insert=True)
    if len(gallery.photos.all()) == 1:
        gallery.head = photo
        gallery.save()
    return photo


def VerifyPhotos(token):
    phs = Photo.objects.filter(token=token).all()
    for ph in phs:
        ph.verified = True
        ph.save()


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
