"""
You need to create a calculator function, but the calculator function has to
take the value from the parameterized constructor. So while creating the object,
you will pass the parameters and that will basically return the sum of the two numbers,
multiplication of two numbers.
"""

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculator(self):
        print(self.a + self.b)
        print(self.a * self.b)

c = Calc(5, 6)
c.calculator()