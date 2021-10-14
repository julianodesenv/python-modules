from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import charset
import smtplib

charset.add_charset('utf-8', charset.QP, charset.QP, 'utf-8')

email = ''
password = ''

with open('./006 - String and template/template.html', 'r') as html:
    template = Template(html.read())

    date = datetime.now().strftime('%Y-%m-%d')
    body_msg = template.safe_substitute(name='Juliano', date=date)

msg = MIMEMultipart()
msg['from'] = 'Juliano Monteiro'
msg['to'] = email
msg['subject'] = 'Assunto e-mail Ação'

body = MIMEText(body_msg, 'html', 'UTF-8')
msg.attach(body)

#with open('./006 - String and template/img-test.png', 'rb') as img:
#    img = MIMEImage(img.read())
#    msg.attach(img)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, password)
        smtp.send_message(msg)
        print("Email enviado com sucesos!")
    except Exception as e:
        print("Email não enviado")
        print("Erro:", e)