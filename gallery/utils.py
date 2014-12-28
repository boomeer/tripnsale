from gallery.models import *
from util.utils import GetNewId
from PIL import Image
import os
from django.core.files import File
from datetime import datetime
from util.utils import TsExc


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
    if gallery.photos.filter(verified=True).count() \
        + gallery.photos.filter(verified=False, token=token).count() >= 10:
        raise TsExc("image_limit_exceeded")
    photo = Photo(
        gallery=gallery,
        token=token,
        verified=False,
    )
    photo.save(force_insert=True)
    if not gallery.head:
        gallery.head = photo
        gallery.save()
    return photo


def VerifyPhotos(token):
    phs = Photo.objects.filter(token=token).all()
    for ph in phs:
        ph.verified = True
        ph.save()


def StoreImage(image, field, sizeLimit=6*2**20):
    imageFileExt = os.path.splitext(image.name)[1]
    if imageFileExt not in [".jpg", ".jpeg", ".gif", ".png"]:
        raise TsExc("image_bad_format")
    if image.size > sizeLimit:
        raise TsExc("image_big_size")
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
