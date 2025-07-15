import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Rafael Montiel'
email['to'] = 'salvoperez51@gmail.com'
email['subject'] = 'You won a million dollars'

email.set_content(html.substitute(name='Peter'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('salvoperez51@gmail.com', 'cqnn yyiu erie fhfz')
    smtp.send_message(email)
    print('all good boss')