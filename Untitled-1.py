def namecheck(word, currentitem):
    hasletter = False
    hasnumber = False
    if len(word) < 8:
        print("Your "+currentitem+" must be at least 8 characters long")
        return False
    else:
        for char in word:
            if char.isdigit():
                hasnumber = True
                break
            else:
                hasnumber = False
        for char in word:
            if char.isalpha():
                hasletter = True
                break
            else:
                hasletter = False
    if hasletter == True and hasnumber == True:
        print("This is a valid "+currentitem.lower()+".")
        return True
    elif hasletter == True and hasnumber == False:
        print("Your "+currentitem.lower()+ " needs to have at least one number")
        return False
    elif hasletter == False and hasnumber == True:
        print("Your "+currentitem.lower()+ " needs to have at least one letter")
        return False
    else:
        print(currentitem.title()+ " must have letters and numbers")
        return False
        
class user:
    name = " "
    password = " "

user_id = user()

user_id.name = input("What would you like your username to be? ")
while namecheck(user_id.name,"Username") == False:
    user_id.name = input("Please enter a different username: ")

user_id.password = input("What would you like your passowrd to be? ")
while namecheck(user_id.password,"Password") == False:
    user_id.password = input("Please enter a different password: ")

print(user_id.name)
print(user_id.password)

user_name_guess = input("What is your user name? ")
while(user_name_guess.lower() != user_id.name.lower()):
    if user_name_guess.lower() != user_id.name.lower():
        print("This is not a valid username please try another one")
        user_name_guess = input("What is your username? ")

count = 0
user_password_guess = input("What is your password? ")
while (user_password_guess.lower() != user_id.password.lower()):
    count += 1
    user_password_guess = input("Password incorrect please try again: ")
    if count >= 3:
        print("You have attemped to enter in your password too many times. Sorry.")
        exit()
    
    