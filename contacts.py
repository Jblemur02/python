class contact:
    firstname = None
    lastname = None
    birthday = None
    phone = None
    email = None
    address = None
    Notes: None

#def addcontacts():
#    whotoadd = input("Who would you like to add to your contacts book?")
#    with open(filen,"r") as file:
#        for line in name:
#            print(line)

def readcontacts():
    whotocheck = input("Who's information would you like to retrieve? \n")
    with open(filen,"w") as file:
        for line in filen:
            if line[0] == whotocheck:
                print(line)

print("Hello welcome to the contacts book")


name = input("What is your name?\n"); 
filen = name; filen += ".csv"; filen = filen.lower()
with open(filen,"r") as file:
    for line in name:
        print(line)
        
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