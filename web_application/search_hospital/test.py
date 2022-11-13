import base64
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(from_add, to_add, password, sub, msg):
    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = sub

    msg.attach(MIMEText(msg, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(from_add, password)
        server.sendmail(from_add, msg['To'], msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Error' + str(e))
        return False


send_mail('sojib.24csedu.037@gmail.com', 'hasibulislam756@gmail.com', '', 'this is sub', 'this is message')