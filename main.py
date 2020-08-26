from calculator import _Calculator
import sys

calc=_Calculator()
print("******************************This is a calculator program**************************")



# def _calcuate(number1,number2,operator):
#     switcher={
#         "+":number1+number2,
#         "-":number1-number2,
#         "/":number1/number2,
#         "*":number1*number2
#     }
#     return switcher.get(operator,"Invalid Operation");

def _calculate(number1,number2,operator):
    switcher={
        "+":calc.add(number1,number2),
        "-":calc.subtract(number1,number2),
        "/":calc.divide(number1,number2),
        "*":calc.multiply(number1,number2)
    }
    return switcher.get(operator,"Invalid Operation");


def calculator():
    while(True):
        inp1=int(input("number 1 : "))
        inp2=int(input("number 2 : "))
        operator=input("operation : ")
        print(_calculate(inp1,inp2,operator))
        if(input()=="exit"):
            break;

if __name__=="__main__":
    calculator()
