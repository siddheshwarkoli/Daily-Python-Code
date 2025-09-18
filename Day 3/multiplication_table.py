# Write a Python program that asks the user to enter a number and then prints the multiplication table for that number from 1 to 10.

# 1st Method
'''
num = int(input("Enter a number:"))
print("Multiplication Table of ",num)
for i in range(1,11):
    print(num,"x",i,"=",(num*i))
'''
# ------------------------------------------------------

# 2nd Method
'''
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(f"{num}x{i}={num*i}")
    i=i+1
'''
# ----------------------------------------------------

#3rd Method
def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
    return
num=int(input("Enter a Number"))
table(num)