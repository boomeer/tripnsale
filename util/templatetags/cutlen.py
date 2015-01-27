from django import template
from datetime import datetime
import os.path
import tripnsale.settings as settings

register = template.Library()

@register.filter()
def cutlen(text, l):
    l = int(l)
    if len(text) <= l:
        return text
    else:
        return text[:l-3] + " ..."

@register.filter()
def cutlenw(text, l):
    l = int(l)
    if len(text) <= l:
        return text

    ret = text[:l-3]
    while len(ret) and not ret[-1].isalnum():
        ret = ret[:-1]

    if len(ret) / (l - 3) < 0.5:
        return cutlen(text, l)
    else:
        return ret + " ..."
