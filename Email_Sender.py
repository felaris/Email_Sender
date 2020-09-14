import smtplib

sender = input("Enter Sender's Email :\n")
sender = str(sender)

password = input("Enter Sender's Password :\n")

to = input("Enter Reciepient Email :\n")
to = str(to)


content = input(" Enter Content :\n")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,to,content)
    server.close()

sendEmail(to,content)