
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'type ur email here'
EMAIL_PASSWORD = 'type ur password here'

contacts = ['may0b0t939@gmail.com', 'Necroxz@yahoo.com.sg']

msg = EmailMessage()
msg['Subject'] = 'CHANGE THIS'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '???@example.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
<h2>LOL</h2>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("note: you must change the smtp.gmail.com if you want to use a non gmail account")
print("for further details click here: https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=441s")