import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

user_name = os.getenv('SMTP_USER')
passwd = os.getenv('SMTP_PASS')

def send_mail(to, subject, message):
    msg = MIMEMultipart()
    msg['From'] = user_name
    msg['To'] = to 
    msg['Subject'] = subject

    message = MIMEText(message, 'html')
    msg.attach(message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user_name, passwd)
    server.sendmail(user_name, to, msg.as_string())
    server.close()