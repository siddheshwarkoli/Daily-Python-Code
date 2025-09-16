# 1st Method
'''
import math
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
def hcf(a,b):
    return math.gcd(a,b)
print(hcf(a,b))
'''
#--------------------------------------------------

# 2nd Method
'''
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
def hcf(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print("Highest Common factor of given number is",(hcf(a,b)))
'''
#--------------------------------------------------

# 3rd Method
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print("Highest Common factor of given number is",hcf)