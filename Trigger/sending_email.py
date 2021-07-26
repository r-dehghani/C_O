import smtplib

sender_email = "r.dehghani.68@gmail.com"
receiver_email = "r.dehghani.90@gmail.com"
password = "Password-68_"
message = "Hey this is from python!"

server = smtplib.SMTP('smtp.gmail.com' , 587 )
server.starttls()
server.login(sender_email , password)
print("login success")
server.sendmail(sender_email , receiver_email , message)
print("email has been sent to the receiver email !!")