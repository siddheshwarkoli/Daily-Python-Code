# 1st Method
'''
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of ",num," is ",fact)
'''
#--------------------------------------------------

# 2nd Method
'''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("Enter a number: "))
print(fact(n))
'''
#--------------------------------------------------

# 3rd Method
'''
import math
def fact(num):
    fact=math.factorial(num)
    return fact
num=int(input("Enter a number: "))
print(fact(num))
'''
#--------------------------------------------------

# 4th Method
def fact(num):
    fact=1
    while num>1:
        fact=fact*num
        num=num-1
    return fact
num=int(input("Enter a number: "))
print(fact(num))