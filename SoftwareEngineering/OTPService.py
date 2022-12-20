import random
import smtplib
import GetPass as G

class OTPService:
    #Private attribute | starts with (__)
    __Email = G.E_Mail
    __Pass = G.Pass

    # __init__ is constructor.
    def __init__(self):

        
        OTP = self.__genrateOTP()
        Name,Email_ID = self.__getData()

        #Validation Function
        self.__validation(OTP,Name,Email_ID)

        #SendMail Function
        self.__sendMail(Name,Email_ID,OTP)

        #PutData function for displaying output.
        self.__putData(Name,Email_ID,OTP)
        

    #Private Methods | starts with(__)
    #Genrate OTP function.
    def __genrateOTP(self):
        Length = int(input("Enter Length of OTP: "))
        otp = ''.join([str(random.randint(0,9)) for i in range(Length)]) #Generated OTP using random.randint()
        return otp

    # Get Method is used for getting input from user.
    def __getData(self):
        Name = input("Enter Name of Receiver: ")
        Email_ID = input("Enter Email ID of Receiver: ")
        return Name,Email_ID

    # Put method is used for displaying output to user.
    def __putData(self,Name,Email_ID,OTP):
        # This will only display if there is no errors
        print("\nName of Receiver is: ",Name)
        print("Email ID of Receiver is: ",Email_ID)
        print("OTP: ",OTP)
        print("Email is Sent!")
        
        

    def __sendMail(self,Name,Email_ID,OTP):
        server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
        # Adding transfer layered security
        server.starttls()
        server.login(self.__Email,self.__Pass) # Email, App password are inserted.
        msg = 'Subject: Sending Mail using Python (smtplib)!\n\nHello '+Name+', Your OTP is '+str(OTP)
        #Inserted Sender email ID, Recevier email ID.
        server.sendmail(self.__Email,Email_ID,msg)
        server.quit() #Quits Server

    def __validation(self,OT,Name,Email_ID):
        OTP = OT
        assert len(OTP) in range(4,9),"Invalid Length"
        assert "gmail" in Email_ID and "@" in Email_ID and "." in Email_ID and ".com" in Email_ID,"Invalid Email ID"
        return OTP

    # Destructor
    def __del__(self):
        print("Destructor called, Object is Deleted")


print("""\
        Features of OOP i have used in this program are as follows:
        1. Class and Instances
        2. Private Members,methods
        3. Data Encapsulation
        4. Get and Put method
        5. Default Constructor
        6. Assertion Error
        7. Data Hiding
        8. Destructor
        \n
    """)

#Created Objects of Class
O1 = OTPService()
print()
O2 = OTPService()

#Destructor is called
del O2 


