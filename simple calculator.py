def calculator():
    print("Simple Calculator")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
    print("Type 'exit' to quit\n")
    
    while True:
        # Get user input
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            break
        
        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            break
        
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            break
        
        try:
            # Convert inputs to numbers
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero!\n")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Please use +, -, *, or /\n")
                continue
            
            # Display result
            print(f"Result: {num1} {operator} {num2} = {result}\n")
            
        except ValueError:
            print("Invalid number input! Please enter numeric values.\n")

if __name__ == "__main__":
    calculator()
    print("Calculator closed. Goodbye!")