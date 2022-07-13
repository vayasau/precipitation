# siuncia zinute i e. pasta

import smtplib
from credential import username, password, sender


def send_mail(mail, text, gps):
    from_mail = sender
    to  = mail
    subj = text
    message_text = f"Have a good day in {gps}"
    msg = f"From: {from_mail}\nTo: {to}\nSubject: {subj}\n\n{message_text}"

    try:
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_mail, to, msg)
        server.quit()
    except:
        print("Message not sent.")
