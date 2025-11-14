from queue import PriorityQueue

nam=input("Please enter your name \n")

def palindrom(st):
    if st == st[::-1]:
        print("It is a pallindrome")
    else:
        print("it is not a pallindrome")

palindrom(nam)