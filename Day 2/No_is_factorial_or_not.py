# 1st Method
'''
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    if fact==n:
        print(n," is factorial of ",i)
        break
    elif fact>n:
        print(n,"is not a factorial of any number.")
        break
'''
# ------------------------------------------------------

# 2nd Method
'''
n=int(input("Enter a number: "))
fact=1
i=1
while fact<n:
    i=i+1
    fact=fact*i
if fact==n:
    print(n," is a factorial of ",i)
else:
    print(n," is not a factorial of any integer")
'''
# -------------------------------------------------------

# 3rd Method
n=int(input("Enter a number: "))
a=n
i=2
while n > 1:
    if n%i!=0:
        break
    n=n//i
    i=i+1
if n==1:
    print(a," is a factorial of ",(i-1))
else:
    print(a," is not a factorial of any integer")