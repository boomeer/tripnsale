from django.shortcuts import render
from django.http import JsonResponse
from util.utils import SafeView
from gallery.models import *
from gallery.utils import *


@SafeView
def GalleryAddPhotoView(request):
    params = request.REQUEST
    gallery = Gallery.objects.get(token=params.get("gallery", ""))
    photoToken = params.get("token")
    files = []
    for photo in request.FILES.getlist("photos"):
        ph = CreateGalleryPhoto(gallery, photoToken)
        try:
            filePath = StoreImage(photo, ph.img)
            MakeThumbnail(ph.img, ph.thumbnail)
            ph.save()
            files.append({
                "name": filePath,
                "thumbnailUrl": ph.img.url,
            })
        except:
            files.append({
            })
            ph.delete()
    return JsonResponse({
        "files": files,
    })

