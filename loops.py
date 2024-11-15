num = int(input("Please enter a positive number"))
if num < 0:
    print("That was not a positive number, enter a positive number")
else:
    factorial=1
    for i in range (1, num+1):
        factorial = factorial*i
        print("the factorial of all numbers up to yours is", factorial)
