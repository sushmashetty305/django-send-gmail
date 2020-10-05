import smtplib
import logging

from django.conf import settings

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


def sendEmail(email_to, email_content, email_subject):
    try:
        msg = MIMEMultipart()
        msg["To"] = email_to
        msg["From"] = settings.EMAIL_HOST_USER
        msg["Subject"] = email_subject
        msgText = MIMEText(email_content, 'html')
        msg.attach(msgText)

        emailRezi = smtplib.SMTP_SSL('smtpout.secureserver.net', settings.EMAIL_PORT)
        emailRezi.ehlo()
        emailRezi.set_debuglevel(1)
        emailRezi.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        emailRezi.sendmail(settings.EMAIL_HOST_USER, email_to, msg.as_string())
        emailRezi.quit()
    except Exception as error:
        # print error
        logger.error(error)
