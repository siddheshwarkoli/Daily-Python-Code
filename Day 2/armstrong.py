# Write a Python program to check whether a number entered by the user is an Armstrong number.

# 1st Method
'''
def armstrong(num):
    temp=num
    n=len(str(num))
    result=0
    while temp>0:
        digit = temp%10
        result=result+(digit**n)
        temp=temp//10
    return result==num
num=int(input("Enter a number: "))
if armstrong(num):
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
'''
# ----------------------------------------------------

# 2nd Method
def arm(num):
    digit=str(num)
    n=len(digit)
    result=0
    for i in digit:
        result=result+int(i)**n
    return result == num
num = int(input("Enter a number: "))
if arm(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
