import GetPass #Importing Password,Email From another file.
import random
import smtplib #This library is used for sending message using email.

password = GetPass.Pass
Sender_Mail = GetPass.E_Mail

def genrateOtp():
    Length = int(input("Enter Length of OTP: "))
    otp = ''.join([str(random.randint(0,9)) for i in range(Length)]) #Generated OTP using random.randint()
    return otp

def sendMail(Sender_Mail,password):
    serverLogin(Sender_Mail,password)
    msg = 'Subject: Sending Mail using Python (smtplib)!\n\nHello '+Name+', Your OTP is '+str(genrateOtp())
    #Inserted Sender email ID, Recevier email ID.
    server.sendmail(Sender_Mail,Email,msg)
    print("Email Sent!")

def serverLogin(Sender_Mail,password):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted.
    
Name = input("Enter Receiver's First Name:- ")
Email = input("Enter Reciptant's Email address:- ")




sendMail()
server.quit() #Quits Server
