from django import template
from datetime import datetime
import os.path
import tripnsale.settings as settings
import mail.utils as mail

register = template.Library()

class MailTagsNode(template.Node):
    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text

def _do_mailtags(parser, token, tagText):
    try:
        tagname = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("{} tag requires no arguments".format(token.contents.split()[0]))
    return MailTagsNode(tagText)

@register.tag(name="email_header")
def do_ccstatic(parser, token):
    return _do_mailtags(parser, token, mail.HEADER_TAG[0])

@register.tag(name="email_endheader")
def do_ccstatic(parser, token):
    return _do_mailtags(parser, token, mail.HEADER_TAG[1])

@register.tag(name="email_content")
def do_ccstatic(parser, token):
    return _do_mailtags(parser, token, mail.CONTENT_TAG[0])

@register.tag(name="email_endcontent")
def do_ccstatic(parser, token):
    return _do_mailtags(parser, token, mail.CONTENT_TAG[1])
