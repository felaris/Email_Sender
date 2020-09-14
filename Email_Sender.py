import smtplib

sender = input("Enter Sender's Email")
sender = str(sender)

password = input("Enter Sender's Password")

to = input("Enter Reciepient Email")
to = str(to)


content = input(" Enter Content")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender,password)
    server.sendmail