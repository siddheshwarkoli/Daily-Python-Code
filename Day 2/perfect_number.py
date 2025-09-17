# 1st Method
'''
def perfect(n):
    div=0
    for i in range(1,n):
        if n % i == 0:
            div=div+i
    return div==n
num=int(input("Enter a number: "))
if perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
'''
# ------------------------------------------------------

# 2nd Method
'''
import math
def perfect(n):
    if n<=1:
        return False
    div=1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            div=div+i
            if i!=n//i:
                div=div+n//i
    return div==n
num=int(input("Enter a number: "))
if perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
'''
# ------------------------------------------------------

# 3rd Method
def sum(n,i=1):
    if i ==n:
        return 0
    if n%i==0:
        return i+sum(n,i+1)
    return sum(n,i+1)
def perfect(n):
    return sum(n)==n
num=int(input("Enter a number: "))
if perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
