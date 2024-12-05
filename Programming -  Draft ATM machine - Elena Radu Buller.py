print("Welcome to ERB_Bank")
attempts = 3
CorrectPin = 2506
balance = 500
while attempts != 0:
    pin = int(input("Please enter the correct 4-digit pin."))
    if pin != CorrectPin:
          print ("Your pin is incorrect!")
          attempts -=1
          if attempts == 0:
              print("You have no more attempts left, start again!")
              break
    else:
        print ("You entered the correct pin!")
        
        
        
