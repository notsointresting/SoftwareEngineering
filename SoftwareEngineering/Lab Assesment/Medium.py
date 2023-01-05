from email.message import EmailMessage # It provides creating or modifying structured messages.
import imghdr  # The imghdr module determines the type of image 
import os 
from PIL import Image  #PIL is Python Image Library
import pywhatkit  # Ro Send Message on whatsapp, Pywhatkit library is used.
import smtplib 
import urllib.request# request module defines functions and classes which help in opening URLs
import Getpass as G
import Context as C


msg = EmailMessage()
Sender_Mail = G.Mail
password = G.PassWord


def sendMail(Name,Reciver_Mail,Text):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted.

        
    msg['Subject'] = 'Testing of HBD Service!'
    msg['From'] = Sender_Mail
    msg['To'] = Reciver_Mail
    
    msg.set_content(f'Happy birthday {Name}!\n{Text}')
    
    urllib.request.urlretrieve('https://thumbs.dreamstime.com/b/colorful-happy-birthday-cupcakes-candles-spelling-148323072.jpg',"HBD.jpg")
    
    with open('HBD.jpg','rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        
        
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename= file_name)
    server.send_message(msg)
    
    server.quit()
    del msg['From']
    del msg['Subject']
    del msg['To']
    msg.clear_content()

def sendWTPM(Name,Number,Text):
    img = 'HBD.jpg'
    body = f'Happy birthday {Name}!\n{Text}.'
    pywhatkit.sendwhats_image(Number,img,body,15,False,3)


#FM: Festival Message
def sendFM(Reciver_Mail,Name):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted.

        
    msg['Subject'] = 'Testing of Festival Service!'
    msg['From'] = Sender_Mail
    msg['To'] = Reciver_Mail

    
    msg.set_content(C.GetContext(Name),subtype='html')
 
    
    #urllib.request.urlretrieve('https://www.mynameart.com/user-upload/63a72cdb8a9f6.jpg',"MerryChristmas.jpg")
    
    with open('result.jpg','rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        
        
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename= file_name)
    server.send_message(msg)
    
    server.quit()
    del msg['From']
    del msg['Subject']
    del msg['To']
    msg.clear_content()

##def sendFMWT(Number,Text):
##    Photo = 'MerryChristmas.jpg'
##    body = f'{Text}'
##    pywhatkit.sendwhats_image(Number,Photo,body,15,False,3)
    



