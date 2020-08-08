num1 = float(input("enter first number"))
oper = input("enter operator")
num2 = float(input("enter second number"))
if oper == '*':
    print(num1 * num2)
elif oper == '+':
    print(num1 + num2)    
elif oper == '-':
    print(num1 - num2)
elif oper == '/':
    print(num1 / num2)
else:
    print("worng operator is inserted")                    
