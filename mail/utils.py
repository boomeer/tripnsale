import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import tripnsale.settings as settings


def SendMail(fr, to, msg):
    try:
        sm = smtplib.SMTP("localhost")
        sm.sendmail(fr, to, msg.encode("utf-8"))
        sm.quit()
    except:
        raise
        
