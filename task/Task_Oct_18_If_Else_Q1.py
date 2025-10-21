# Question 1. : Given a Number a number you need to calculate the factorial of that number

# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

a = int(input("Enter the number: "))
b = a
factorial = 1
if a == 0:
    print(f"The factorial of {b} is {1}")
elif a > 0:
    while a != 0:
        factorial *= a
        a = a -1
    print(f"The factorial of {b} is {factorial}")
else:
    print("Please enter a positive number")