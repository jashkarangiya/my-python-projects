import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "XYZ"
msg['From'] = "Jinesh Dolia"
msg['To']= "Jash Karangiya"

with open('emailTemplate.txt') as myfile:
    data= myfile.read()
    msg.set_content(data)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("xyz@gmail.com", "abc@gmail.com")
    server.sendmail(msg)

print("Email sent!!")
