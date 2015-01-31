import re
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import tripnsale.settings as settings

_URL_RE_STR = \
    r'\b(?P<url>' + \
        r'(?P<domain>' + \
            r'(?:https?://|www\.)(?:[\w\d\-_]{2,50}\.)+(?:[\w]{2,50})(?::\d+)?|' + \
            r'(?:https?://)?(?:www\.)?tripnsale\.com(?::\d+)?' + \
        r')' + \
        r'(?P<path>' + \
            r'(?P<basepath>(?:/[\w\d\-_]+)*/?)' + \
            r'(?P<params>|\?[\w\d=+&-_%]+)' + \
            r'(?P<hash>|#[\w\d\-_]*)' + \
        r')' + \
    r')\b'

URL_RE = re.compile(_URL_RE_STR)
LINK_RE = re.compile(r'<a +href="(?P<url>.*?)">(?P<content>.+?)</ *a>')
