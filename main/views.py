from django.shortcuts import render
from util.utils import (
    SafeView,
    RenderToResponse,
    CheckPost,
)


@SafeView
def MainView(request):
    return RenderToResponse("main/main.html", request, {
        "url": "/",
    })
