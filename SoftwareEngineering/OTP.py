import unittest
import smtplib
import Send_OTP_Using_Mail_2 as O
import time

class BetweenAssertMixin(object):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (x, low, hi))

    
        
class OTP(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        print("------------------------------------TestCase No.1-------------------------------------")
        # This is valid TestCase
        Name = "Sahiil"
        Email = "Sahiilshriwardhankar@gmail.com"

        #Validation of Email
        O.EmailValidation(Email)

        #Checking OTP
        otp = O.genrateOtp()        
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)

        

        #Validation of OTP
        O.validateOTP(otp)
            
        

    def testcase2(self):
        print("------------------------------------TestCase No.2-------------------------------------\n")

        # Email Validation
        # Here i provided, incorrect Email ID.
        Name = "Sahiil"
        Email = "Sahiilshriwardhankargmail.com"

        #Validation of Email
        O.EmailValidation(Email)
            

        #Checking OTP
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)

        #Validation of OTP
        O.validateOTP(otp)

        print("---------------------------------------------------------------------------------------\n")
        

    def testcase3(self):
        print("------------------------------------TestCase No.3-------------------------------------\n")

        # There is no 
        Name = "Sahiil"
        Email = "Sahiilshriwardhankar@gmail.com"

        #Validation of Email
        O.EmailValidation(Email)

        # Checking OTP
        # Here i will Enter invalid otp length
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)
        
        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)

        #Validation of OTP.
        O.validateOTP(otp)
       

    def testcase4(self):
        print("------------------------------------TestCase No.4-------------------------------------\n")
        
        #Checking Email
        Name = "Sahiil"
        Email = "Sahiilshriwardhankar@gmail.com"

        #Validation of Email
        O.EmailValidation(Email)

        #Checking OTP
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)
        
        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)

        #Validation of OTP and I will take time greater then 30sec.
        O.validateOTP(otp)

        

        print("---------------------------------------------------------------------------------------\n")
        
        
unittest.main()
time.sleep(50)
    
