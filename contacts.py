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
    
def readcontacts():
    whotocheck = input("Who's information would you like to retrieve? \n")
    with open(filen,"w") as file:
        for line in filen:
            if line[0] == whotocheck:
                print(line)

print("Hello welcome to the contacts book")

name = input("What is your name?\n"); 
filen = name; filen += ".csv"; filen = filen.lower()

whattodo = None
whattodo = input("Hello "+name+" what would you like to do? \n1.Check contacts \n2.Add contacts \n3.Exit \n")
while whattodo != "1" and whattodo != "2" and whattodo != "3": 
    whattodo = input("Please enter the number 1, 2 or 3\n")

if whattodo == "1":
    readcontacts()
elif whattodo == "2":
    addcontacts()
else:
    exit()