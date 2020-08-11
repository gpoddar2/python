# coordinates = (4,5) tuple cannot be change
coordinates = [4,5]
coordinates[1] = 10 
print(coordinates[1])

enter = (input("enter a letter"))
win = enter[::-1]
print(win)

if enter == win:
    print("Palindrom")
else:
    print("not palindrome")