# 1st Method
'''
num=int(input("Enter a number: "))
if num==1:
    print(num," is not a prime number")
elif num<=0:
    print("Enter a positive number")
else:
    for i in range(2,num):
        if num%i==0:
            print(num," is not a prime number")
            break
    else:
        print(num," is a prime number")
'''
#--------------------------------------------------

# 2nd Method
'''
num=int(input("Enter a number: "))
def prime(num):
    if num<=1:
        print(num," is not a prime number")
        return
    for i in range(2,num):
        if num%i==0:
            print(num," is not a prime number")
            return
    print(num," is a prime number")
prime(num)
'''
#--------------------------------------------------

# 3rd Method
import math
num=int(input("Enter a number: "))
def prime(num):
    if num<=1:
        print(num," is not a prime number")
        return
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            print(num," is not a prime number")
            return
    print(num," is a prime number")
prime(num)