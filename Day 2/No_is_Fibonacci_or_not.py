# Check give number is fibonacci or not 

# 1st Method
'''
import math
n=int(input("Enter a number: "))
x1=5*n*n+4
x2=5*n*n-4
sq1=int(math.sqrt(x1))
sq2=int(math.sqrt(x2))
if ((sq1*sq1)==x1 or (sq2*sq2)==x2):
    print(n,"is a fibonacci number.")
else:
    print(n,"is not a fibonacci number.")
'''
# --------------------------------------------------

# 2nd Method
import math
def fibo(n):
    def sq(x):
        s=int(math.sqrt(x))
        return s*s==x
    return sq(5*n*n+4) or sq(5*n*n-4)
num=int(input("Enter a number: "))
if fibo(num):
    print(num,"is a fibonacci number.")
else:
    print(num,"is not a fibonacci number.")