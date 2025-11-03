"""
Q - Create a function which will take the 3 values from the user, which are length of the
triangle.  side1, side2, side2
i/p - int side1 == side2 =side3 → isoceles
o/p = result in string - iso, eq, scalene
"""

def triangle(side1, side2 ,side3):
    if side1 == side2 == side3:
        print("Triangle is equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Triangle is isosceles")
    else :
        print("triangle is scalene")

triangle(12,13,15)
triangle(12,12,12)
triangle(15,15,13)