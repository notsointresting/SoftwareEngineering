import GetPass as G #Importing Password,Email From another file.
import random
import smtplib #This library is used for sending message using email.


password = G.Pass
Sender_Mail = G.E_Mail
otp = ''.join([str(random.randint(0,9)) for i in range(4)]) #Generated OTP using random.randint()
server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API

# Adding transfer layered security
server.starttls()
print(Sender_Mail,password)
server.login(Sender_Mail,password) # Email, App password are inserted.

Name = input("Enter Receiver's First Name:- ")
Email = input("Enter Reciptant's Email address:- ")





msg = 'Subject: Sending Mail using Python (smtplib)!\n\nHello '+Name+', Your OTP is '+str(otp)

#Inserted Sender email ID, Recevier email ID.
server.sendmail(Sender_Mail,Email,msg)
print("Email Sent!")
server.quit() #Quits Server
