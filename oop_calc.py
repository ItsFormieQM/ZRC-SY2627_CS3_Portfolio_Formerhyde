# type:ignore
import math
import os

class Operators:
    
    def __init__(self):
        pass
        
    def calc_result(self,op,_term_1,_term_2):
        
        match op:
            case "+":
                return round(_term_1 + _term_2)
            case "-":
                return round(_term_1 - _term_2)
            case "*":
                return round(_term_1 * _term_2)
            case "/":
                if _term_2 == 0:
                    return "Undefined"
                else:
                    return round(_term_1 / _term_2)
            case _:
                print("The operator is not valid!")
                main()
            
def main():
    obj_math = Operators()
    _arg_1 = None
    _arg_2 = None
    op = None

    while True:
        try:    
            _arg_1 = float(input("Enter the first number: "))
            _arg_2 = float(input("Enter the second number: "))
            op = input("Enter operator (+,-,*,/): ")
            break
        except ValueError:
            print("Please input in a number!")
            
    print(f"Result is around: {obj_math.calc_result(op,_arg_1,_arg_2)}")
    os._exit(0)
    
main()

                        
