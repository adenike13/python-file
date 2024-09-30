# simple calculator

operation = input()

def calculator():
    print("select an operation")

    print("1. addition")
    print("2. subtraction")
    print("3. division")
    print("4. multiplication")

    operation = input()  
    
    num1 = input("enter first number: ")
    num2 = input("enter second number:")
    
    if operation == "1":
        print("the sum is " +str(int(num1) + int(num2)))
    elif operation == "2":
        print("the sum is " + str(int(num1) - int(num2)))
    elif operation == "3":
        print("the sum is " + str(int(num1) / int(num2)))
    elif operation == "4":
        print("the sum is " + str(int(num1) * int(num2)))
    else:
        print("invalid")
            
    repeat = input("do you want to perform another operation").lower()
    
    if repeat == 'yes':
        calculator()
    else:
        print("Good day")
            
calculator()
                    

