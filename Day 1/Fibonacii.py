# Write a Python program to print the Fibonacci sequence up to n terms.

# 1) Without using function
'''
n=int(input("Enter a number: "))
a=0
b=1
c=0
while(n>c):
    print(c,end=' ')
    a=b
    b=c
    c=a+b
    '''
# ------------------------------------------------------------

# 2) Using Function and while loop
'''
def fibo(n):
    a,b=0,1
    c=0
    while(c<n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
    return c
n=int(input("Enter a number: "))
result=fibo(n)
'''
# ------------------------------------------------------------

# 3) Using For loop

def fibo(num):
    a= 0
    b= 1
    if num <= 0:
        print("Enter a positive number")
    elif num ==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c=a+b
            print(c)
            a=b
            b=c
num=int(input("Enter a number: "))
fibo(num)

# ------------------------------------------------------------

