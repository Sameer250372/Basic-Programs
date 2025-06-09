while True:


    print("Temperature Conversion Program")
    unit=input("enter the unit you want to convert from(C for Celsius, F for Fahrenheit): ").strip().upper()
    if unit == 'C':
        celsius= float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif unit == 'F':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    else:
        print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
