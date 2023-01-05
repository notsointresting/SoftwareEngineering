from datetime import date 
import Medium as M 
import mysql.connector
import Getpass as G #Importing Database and other passwords.
import os
import sys


#It's version 2
#Because i've created database on cloud.




today = date.today() # To get Today's Date.

db=mysql.connector.connect(host=G.HOST,user=G.DB_USER,passwd=G.DB_PASS,database=g.DB_NAME)
cursor=db.cursor()

print('-------------------------------------------Birthday Service and Festival-------------------------------')


G.Menu()
choice = int(input("ENTER YOUR CHOICE---> "))

#To Fetch Data's Records
def showData():
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    for d in data:
       print(d)


    

#To Fetch Festival's Records
def showFestivals():
    cursor.execute('SELECT * FROM Festivals')
    data = cursor.fetchall()
    for d in data:
       print(d)



def getData():
    global Email_ID 
    global Month 
    global Name 
    global Number
    global Holiday
    global Date

    Holiday,Date = [],[]

    Email_ID,Month,Name,Number = [],[],[],[]

    #To get Birthday's table data
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    for d in data:
        Email_ID += [d[1]]
        Month+=[(str(d[2])).split('-')] 
        Name +=  [d[0]]  
        Number += [d[3]]
        print(d)

    #To get Festival's table data
    cursor.execute('SELECT * FROM Festivals')
    data = cursor.fetchall()
    for d in data:
        Holiday += [d[0]]
        Date += [(str(d[1])).split('-')]
    


def checkBirthdayToday():
    getData()
    Flag = False
    Msg = ""
    for i in range(len(Name)):
            
        if str(today.day)== Month[i][0] and str(today.month)==Month[i][1]:
            Flag = True
            print("List of Person's who have birthday today!")
            print(Name[i],"Date:\t",Month[i][0],":",Month[i][1])
            Text = sys.stdin.read()
            
            M.sendMail(Name[i],Email_ID[i],Text) #This will send Mail to the person
            M.sendWTPM(Name[i],Number[i],Text) #This will send Whatsapp Message to the person
    if Flag:
        Msg = "Birthday Message Has been sent!"
    else:
        Msg = "No one's has today birthday!"
    return Msg

def checkFestivalToday():
    getData()
    Msg = ""
    Flag = False
    for i in range(len(Date)):
        for j in range(len(Date[i])):
            
            if str(today.month) == Date[i][j] and str(today.day) == Date[i][j-1]:
                Flag = True
                
                        
                # The for loop will send emails to all present in table of Data.
                for i in range(len(Name)):            
                    M.sendFM(Email_ID[i],Name[i])
                            
                        #The for loop will send Whatsapp Message to all present in table of Data.
                for i in range(len(Number)):
                    M.sendFMWT(Number[i],Text)

    if Flag:
        Msg = "Festival message has been sent!"
    else:
        Msg = "No Festival Today!"
    return Msg

##while choice!=5:
    if choice == 1:
        showData()
    elif choice == 2:
        showFestivals()
    elif choice == 3:
        checkBirthdayToday()
    elif choice == 4:
        checkFestivalToday()
    elif choice == 5:
        break
    else:
        print("Invalid Choice (1-5) only!")
    choice = int(input("ENTER YOUR CHOICE---> "))
print("Thank you for choosing our service!")





                        
                




