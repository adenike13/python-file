print("enter your name")

name = input()

print("you are asked to enter a number ", name )

print("enter first number")
try :
    num = int(input())
    if num % 2 == 1:
        print("You have entered an odd number")
    else:
        print("You have entered an even number")
except ValueError:
    print("Error:You have not entered a number")