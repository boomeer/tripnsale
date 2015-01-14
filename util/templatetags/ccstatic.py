from django import template
from datetime import datetime
import os.path
import tripnsale.settings as settings

register = template.Library()

class CacheCoherentStaticNode(template.Node):
    def __init__(self, path):
        self.path = path
        self.fspath = os.path.join(settings.STATIC_ROOT, self.path)
        self.urlpath = os.path.join(settings.STATIC_URL, self.path)
        try:
            self.modtime = datetime.fromtimestamp(os.path.getmtime(self.fspath))
        except OSError:
            self.modtime = None

    def render(self, context):
        if self.modtime:
            return "{}?mt={}".format(self.urlpath, self.modtime.strftime("%m%d%H%M%S"))
        else:
            return self.urlpath

@register.tag(name="ccstatic")
def do_ccstatic(parser, token):
    try:
        tagname, pathstring = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("{} tag requires a single argument".format(token.contents.split()[0]))
    if not (pathstring[0] == pathstring[-1] and pathstring[0] in ('"', "'")):
        raise template.TemplateSyntaxError("{} tag's argument should be in quotes".format(tag_name))
    return CacheCoherentStaticNode(pathstring[1:-1])

