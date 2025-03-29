import csv
import pandas as pd
import os.path

class contact:
    def __init__(self,firstname,lastname,birthday,phone,email,address,notes):
        self.birthday = birthday
        self.phone = phone
        self.email = email
        self.address = address
        self.notes: notes
        self.firstname = firstname
        self.lastname = lastname

def addcontacts():
    print("Ok we can do that. If you don't have a certain peice of information just press enter.")
    newcontact = contact(None,None,None,None,None,None,None)
    whotoadd = input("What is the first name of the person?")
    newcontact.firstname = whotoadd
    whotoadd = input("What is the last name of the person?")
    newcontact.lastname = whotoadd
    whotoadd = input("What is the address of the person?")
    newcontact.address = whotoadd
    whotoadd = input("What is the email of the person?")
    newcontact.email = whotoadd
    whotoadd = input("What is the phone number of the person?")
    newcontact.phone = whotoadd
    whotoadd = input("Would you like to leave any notes about this person")
    newcontact.notes = whotoadd

    addthis = [newcontact.firstname, newcontact.lastname, newcontact.address, newcontact.address, newcontact.email, newcontact.phone,newcontact.notes]

    with open(filen,"w") as file:
        writer = csv.writer(file)
        writer.writerow(addthis)
        
def readcontacts():
    howmanyf = 0
    fnamelist = []
    whotocheck = input("Who's information would you like to retrieve? \n")
    lowerwhotocheck = whotocheck.lower()
    firstandlastname = lowerwhotocheck.split(" ")
    with open(filen, "r") as f:
        for row in f:
            if row[0] == firstandlastname[0]:
                addfirstandlast = row[0] +" "+ row[1]
                howmanyf += 1
                fnamelist.append(addfirstandlast)
            else:
                continue
    if howmanyf == 0:
        print("There are currently "+str(howmanyf)+" people in yur contacts book with the first name of "+firstandlastname[0])
        shouldcheck = input("Would you like to check these names?")
        if shouldcheck.lower() == "y" or shouldcheck.lower() == "yes":
            print()
        
print("Hello welcome to the contacts book")

name = input("What is your name?\n"); 
filen = name; filen += ".csv"; filen = filen.lower()

df = pd.read_csv(filen)
if df.empty == False:
    with open(filen, 'w') as file:
        fieldnames =  ["First Name", "Last Name", "Address", "Email", "Phone", "Notes"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
else:
    pass

whattodo = input("Hello "+name+" what would you like to do? \n1.Check contacts \n2.Add contacts \n3.Exit \n")
while whattodo != "1" and whattodo != "2" and whattodo != "3": 
    whattodo = input("Please enter the number 1, 2 or 3\n")

if whattodo == "1":
    readcontacts()
    addmore = input("Would you like to add more contacts to your file?"); addmore = addmore.lower()
    if addmore == "y" or addmore == "yes":
        addcontacts()
    else:
        readfile = input("Ok, would you like to check on any of your contacts?")
        if readfile == "y" or readfile == "yes":
            readcontacts()
        else:
            print("Have a nice day "+name)
elif whattodo == "2":
    addcontacts()
else:
    exit()