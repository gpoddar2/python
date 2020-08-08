string = input("enter a number")
txt = string[::-1]
print(txt)
if string == txt:
    print("given number palindrome")
else:
    print("given number is not plaindrome")    