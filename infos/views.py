from django.shortcuts import render
from util.utils import RenderToResponse


def InfoView(request, name):
    return RenderToResponse("infos/with_base.html", request, {
        "filepath": "infos/{}.html".format(name),
    })
