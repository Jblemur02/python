print("Hello welcome to the calculator")
whattodo = input("What would you like to do? \n1.Multiply\n2.Divide\n3.Subtract\n4.Add\n")

while whattodo != "1" and whattodo != "2" and whattodo != "3" and whattodo != "4":
    whattodo = input("Please enter a number between 1 and 4\n")

if whattodo == "1":
    num1 = float(input("What is the first number?\n"))
    num2 = float(input("What is the second number?\n"))
    print("The answer is: " , num1 * num2)
elif whattodo == "2":
    num1 = float(input("What is the first number?\n"))
    num2 = float(input("What is the second number?\n"))
    print("The answer is: " , num1 * num2)
elif whattodo == "3":
    num1 = float(input("What is the first number?\n"))
    num2 = float(input("What is the second number?\n"))
    print("The answer is: " , num1 * num2)
else:
    num1 = float(input("What is the first number?\n"))
    num2 = float(input("What is the second number?\n"))
    print("The answer is: " , num1 * num2)