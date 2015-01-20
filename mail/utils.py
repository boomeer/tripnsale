import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import tripnsale.settings as settings


def SendMail(user, msg):
    if not user.emailNotify:
        return
    fr = "info@tripnsale.com" # FORCE, yep
    try:
        sm = smtplib.SMTP("localhost")
        sm.sendmail(fr, user.email, msg.encode("utf-8"))
        sm.quit()
    except:
        raise
        
