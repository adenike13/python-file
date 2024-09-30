def calculator():
    print("a simple calculator")
    
    print("this is a basic calculator")
    print("you are asked to choose a number")
    num1 = int(input())
    print("you are asked to choose a second number")
    num2 = int(input())
    print("choose an operation")
    print("1 = addition")
    print("2 = subtraction")
    print("3 = multiplication")
    print("4 = division")
    
    print("")
    
    print("choose an operation you would like to use")
    operation = int(input())
    if operation == 1:
        num1 + num2 
        print("your answer is", num1 + num2)
        
    elif operation == 2:
        print("your answer is", num2 - num1)
        
    elif operation == 3:
        print("your answer is", num1 * num2)
        
    elif operation == 4:
        
     try :
        print(num2 / num1)
     except ZeroDivisionError:
      print("error:your cant divide zero")
    
     again = input("do you want to continue: ").lower()
     if again == "yes":
        calculator()
    else:
        print("good day")
calculator()