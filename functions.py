def temp_conversion():
    temp_type = input("Enter your type of conversion (C to F or F to C)")

    if temp_type == 'C to F' or 'c to f':
        celsius = float(input("Enter your temperature"))
        fahrenheit = (celsius*9/5)+ 32
        print("Your temperature in fahrenheit is" , fahrenheit)
        
    elif temp_type == 'F to C' or 'f to c':
        fahrenheit = float(input("Enter your temperature"))
        celsius = 5/9 *(fahrenheit - 32)
        print("Your temperature in celsius is", celsius)
        
    else:
        print("Invalid entry, try again")
                      
temp_conversion()




