num1 = input("Please enter your first number ")
num2 = input("Please enter your second number ")
#isnumeric function finds out if the input is a number
if(num1.isnumeric()and num2.isnumeric()) :
    print("What operation would you like to use?")
    op = input("Please type a for addition, s for subtraction, m for multiplication, or d for division ")
    if(op == "a" or op == "A") :
        answer = int(num1) + int(num2)
        print(answer)
    elif(op == "s" or op == "S") : 
        answer = int(num1) - int(num2)
        print(answer)
    elif(op == "m" or op == "M") :
        answer = int(num1) * int(num2)
        print(answer)
    elif(op == "d" or op == "D") :
        answer = int(num1 / int(num2))
        print(answer)
    else :
        print("You can't type this letter")
        print("You can only type a, s, m, or d")       
else :
    print("These inputs have to be numbers")
