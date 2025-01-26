number = int(input("Enter no:"))

factorial=1

if number < 0:
    print("factorial does not exist for negative no:")
elif number == 0:
    print("factorial of 0 is 1")
else:
    for i in range( 1,number +1):
        factorial = factorial*i
    print("The factorial of no is:",factorial)



