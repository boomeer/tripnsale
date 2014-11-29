import smtplib
import tripnsale.settings as settings

defmsg = """From: {1} <{0}>
To: <{2}>
Subject: {3}

{4}
"""

def SendMail(receivers, subject, content):
    try:
        sm = smtplib.SMTP("localhost")
        if type(receivers) not in [list, tuple]:
            receivers = [receivers]
        message = defmsg.format(settings.EMAIL_SENDER_MAIL, settings.EMAIL_SENDER_NAME,
                                receivers[0], subject, content)
        sm.sendmail(settings.EMAIL_SENDER_MAIL, receivers, message)
    except:
        raise
        
