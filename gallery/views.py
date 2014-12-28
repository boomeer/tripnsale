from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from util.utils import SafeView
from gallery.models import *
from gallery.utils import *
from util.utils import TsExc
from util.msg import GetGalleryExcMsg


@SafeView
def GalleryAddPhotoView(request):
    params = request.REQUEST
    gallery = Gallery.objects.get(token=params.get("gallery", ""))
    photoToken = params.get("token")
    files = []
    for photo in request.FILES.getlist("photos"):
        ph = None
        try:
            ph = CreateGalleryPhoto(gallery, photoToken)
            filePath = StoreImage(photo, ph.img)
            MakeThumbnail(ph.img, ph.thumbnail)
            ph.save()
            files.append({
                "name": filePath,
                "thumbnailUrl": ph.img.url,
            })
        except TsExc as e:
            files.append({
            })
            if ph:
                ph.delete()
            return JsonResponse({
                "files": [{"error": GetGalleryExcMsg(str(e))}],
            })
    return JsonResponse({
        "files": files,
    })

