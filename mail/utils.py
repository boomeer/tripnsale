import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import tripnsale.settings as settings
import django.template.loader as templates
from util.exc import TsExc
import re

import dkim

HEADER_TAG = ("<<header>>", "<</header>>",)
CONTENT_TAG = ("<<content>>", "<</content>>",)

def _SendMail(user, msg):
    if not user.emailNotify:
        return
    fr = "info@tripnsale.com" # FORCE, yep
    try:
        sm = smtplib.SMTP("localhost")
        sm.sendmail(fr, user.email, msg.encode("utf-8"))
        sm.quit()
    except:
        raise

class InvalidTagErr (MailErr):
    def __init__(self, msg):
        super().__init__(msg)

class InvalidTagsNumber (MailErr):
    def __init__(self, msg):
        super().__init__(msg)

def _ExtractTags(text, tag, exactlyOne=False):
    pos = 0
    ret = []
    while True:
        if len(ret) > 1 and exactlyOne:
            raise InvalidTagsNumber("Expected exactly one tags, got more")
        if tag[0] in text[pos:] or tag[1] in text[pos:]:
            if tag[0] not in text[pos:] or tag[1] not in text[pos:]:
                raise InvalidTagErr("Invalid tag: {} ({}, {})".format(str(tag), tag[0] not in text[pos:], tag[1] not in text[pos:]))
            begpos = text.find(tag[0], pos) + len(tag[0])
            endpos = text.find(tag[1], pos)
            ret.append(text[begpos:endpos])
            pos = endpos + len(tag[1])
        else:
            break

    if exactlyOne and len(ret) == 1:
        return ret[0]
    elif exactlyOne:
        return None
    else:
        return ret

class NoMailContent (MailErr):
    def __init__(self, msg):
        super().__init__(msg)

def SendMail(to, template, params={}, templateFromFile=True, dkimKeys=None, dkimSelector=None):
    """
    sends email to @to
    if @templateFromFile == True message will be taken from @template _file_ and
        from @template as a string else.
    template should have header and content section
        (separated with mail.utils.HEADER_TAG, mail.utils.CONTENT_TAG). For example:
        <<header>>
        Sublect: foo
        To: foo@tripnsale.com
        From: bar@tripnsale.com
        <</header>>
        <<content>>
        blahblahblah
        <</content>>
    @params are used tor rendering the template
    @dkimKeys is a pair (private=priv_key, public=pub_key).
        if None, settings.EMAIL_DKIM_KEYS will be taken.
        if there aren't such keys, the mail won't be signed with dkim!
    @dkimSelector is a selector for dkim. if None, settings.EMAIL_DKIM_SELECTOR will be taken
    """
    if not settings.ENABLE_EMAIL:
        return

    fr = "info@tripnsale.com"
    params.update({ "to_email": to,
                    "fr_email": fr })
    if templateFromFile:
        rawmsg = templates.render_to_string(template, params)
    else:
        t = templates.Template(template)
        rawmsg = t.render(templates.Context(params))

    rawmsg = rawmsg.replace("\r\n", "\n")

    rawheaders = _ExtractTags(rawmsg, HEADER_TAG, exactlyOne=True)
    if rawheaders:
        headers = {}
        for rawh in rawheaders.split("\n"):
            if rawh.strip() == "":
                continue
            header = rawh.split(": ")
            if len(header) != 2:
                raise MailErr("Something wrong with header: got {} tokens: {}".format(len(header), header))
            headers[header[0].strip()] = header[1].strip()
    else:
        headers = {}

    content = _ExtractTags(rawmsg, CONTENT_TAG, exactlyOne=True)
    if not content:
        raise NoMailContent("Content is empty")

    msg = MIMEText(content)
    for hname, hval in headers.items():
        msg[hname] = hval

    if dkimKeys:
        rsaKeys = dkimKeys
    elif settings.EMAIL_DKIM_KEYS:
        rsaKeys = settings.EMAIL_DKIM_KEYS
    else:
        rsaKeys = None

    if rsaKeys:
        dkimmsg = dkim.DKIM(str(msg).encode("utf-8"))
        if dkimSelector:
            dkimsel = dkimSelector
        else:
            dkimsel = settings.EMAIL_DKIM_SELECTOR
        dkimsel = dkimsel.encode("utf-8")

        dkimdomain = settings.EMAIL_DKIM_DOMAIN.encode("utf-8")
        dkimkey = rsaKeys.private.encode("utf-8")

        sig = dkimmsg.sign(dkimsel, dkimdomain, dkimkey).decode('ascii')
        sigh, sigc = tuple(sig.split(': ', 1))
        msg[sigh] = sigc

    sm = smtplib.SMTP("localhost")
    sm.sendmail(fr, to, str(msg))
    sm.quit()
