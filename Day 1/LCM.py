# Write a Python program to calculate the LCM (Least Common Multiple) of two positive integers entered by the user.

# 1st Method
import math
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
def lcm(a,b):
    lcm=abs(a*b)//math.gcd(a,b)
    return lcm
print("LCM of given number is ",lcm(a,b))