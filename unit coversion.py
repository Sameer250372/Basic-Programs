def unit_conversion():
    print("Unit Conversion Menu:")
    print("type 'exit' to quit\n")


    while True:
        a=float(input("Enter the value to convert: "))
        if a == 'exit':
            break
        conversion_from=input("unit to converft from (km, m, cm, mm):").lower()
        if conversion_from.lower() == 'exit':
            break
        conversion_to=input("unit to convert to (km, m, cm, mm):").lower()
        if conversion_to.lower() == 'exit':
            break    
        try:
            if conversion_from == 'km':
                if  conversion_to == 'm':
                    result = a*1000
                elif conversion_to == 'cm':
                    result = a*100000
                elif conversion_to == 'mm':
                    result=a*1000000
                else:
                    print("Invalid conversion to unit!")
                    continue
            elif conversion_from == 'm':
                if conversion_to == 'km':
                    result = a / 1000   
                elif conversion_to == 'cm':
                    result = a * 100    
                elif conversion_to == 'mm':
                    result = a * 1000        
                else:
                    print("Invalid conversion to unit!")
                    continue
            elif conversion_from == 'cm':           
                if conversion_to == 'km':
                    result = a / 100000
                elif conversion_to == 'm':
                    result = a / 100
                elif conversion_to == 'mm':
                    result = a * 10
                else:
                    print("Invalid conversion to unit!")
                    continue
            elif conversion_from == 'mm':
                if conversion_to == 'km':
                    result = a / 1000000
                elif conversion_to == 'm':
                    result = a / 1000
                elif conversion_to == 'cm':
                    result = a / 10
                else:
                    print("Invalid conversion to unit!")
                    continue
            print(f"{a} {conversion_from} is equal to {result} {conversion_to}.")
        except ValueError:
            print("Invalid input! Please enter numeric values for the conversion value.\n")    
        
if __name__ == "__main__":
    unit_conversion()
    print("Unit conversion closed. Goodbye!")        