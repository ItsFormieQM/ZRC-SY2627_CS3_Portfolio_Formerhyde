arg1 = 0
arg2 = 0
operator = 0

def Calc():
    global arg1, arg2, operator
    while True:
        try:
            arg1 = float(input("Enter first number: "))
            arg2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number!")
    
    match operator:
        case "+":
            return arg1 + arg2
        case "-":
            return arg1 - arg2
        case "*":   
            return arg1 * arg2
        case "/":
            if arg2 == 0:
                return "Error: Division by zero!"
            else:
                return arg1 / arg2
        case _:
            return "Invalid operator! Please use +, -, *, or /."
        
print("Result: " + str(Calc()))