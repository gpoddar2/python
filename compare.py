num1 = float(input("num one "))
num2 = float(input("num two "))
num3 = float(input("num third "))
if num1 > num2 and num1 > num3:
    print("num1 is the biggest number" + str(num1))
elif num2 > num1 and num2 > num3:
    print("num2 is the biggest number")
else:
    print("num3 is the biggest number")        