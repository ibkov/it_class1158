# -*- coding: utf-8 -*-
"""Send email via smtp_host."""

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

smtp_host = "mail.hosting.reg.ru"
login = "admin@it-class1158.site"
password = "wsx123451"


def send_mail_to_applicant(theme_letter, header_letter, text_letter, recipients_email):
    for email in recipients_email:
        html = f"""\
        <html>
          <head></head>
          <body>
        <img src="https://it-class1158.site/static/images/itclass-logo.png" width="150" height="150">
            <h1 style="text-align: center;">{header_letter}</h1><br>
               <p style="font-size: 18px;">{text_letter}</p>
        <hr>
        <p style="font-size: 18px;">Если у тебя остались какие-то вопросы нажми на вкладку ниже</p>
        <a href="mailto:admin@it-class1158.site?subject=Вопрос от участника">ЗАДАТЬ ВОПРОС</a>
        </p>
          </body>
        </html>
        """
        msg = MIMEMultipart()
        msg['Subject'] = Header(f"{theme_letter}", 'utf-8')
        msg['From'] = login
        msg['To'] = email
        part = MIMEText(html, 'html')
        msg.attach(part)
        s = smtplib.SMTP(smtp_host, 587)
        s.set_debuglevel(1)
        try:
            s.starttls()
            s.login(login, password)
            s.sendmail(login, recipients_email, msg.as_string())
        finally:
            print(msg)
            s.quit()


def send_telegram(text: str):
    token = "ТУТ_ВАШ_ТОКЕН_КОТОРЫЙ_ВЫДАЛ_BotFather"
    url = "https://api.telegram.org/bot"
    channel_id = "@ИМЯ_КАНАЛА"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("hello world!")