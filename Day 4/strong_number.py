# Write a program to check whether a given number is a Strong Number or not.

# Definition: A Strong Number is a number whose sum of the factorial of its digits is equal to the number itself.

# Example: 145 is a Strong Number because
#          1!+4!+5!=1+24+120=145

import math
def strong(num):
    total=0
    temp=num
    while temp>0:
        digit=temp%10
        total=total+math.factorial(digit)
        temp=temp//10
    return total==num
n=int(input("Enter a number: "))
if strong(n):
    print(f"{n} is a Strong number.")
else:
    print(f"{n} is not a Strong number.")