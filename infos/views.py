from django.shortcuts import render
from util.utils import RenderToResponse


def InfoView(request, name):
    return RenderToResponse("infos/{}.html".format(name), request, {})
