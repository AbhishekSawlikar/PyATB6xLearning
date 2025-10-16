# Write a program to check if a number entered by the user is greater than 100.
"""a = 100
b = 75
print("a is greater than b" if a > b else "a is less than b")
"""
# Primary program logic
number = float(input("Enter the Number:"))

if number > 100:
    print("number is greater than 100")
else:
    print("number is less than 100")