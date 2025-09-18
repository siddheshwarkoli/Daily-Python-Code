# Write a Python program that takes three numbers as input from the user and prints the largest of the three.

# 1st Method
'''
n1=float(input("Enter 1st Number: "))
n2=float(input("Enter 2nd Number: "))
n3=float(input("Enter 3rd Number: "))
max=max(n1,n2,n3)
print(max)
'''
# ------------------------------------------------------

# 2nd Method
'''
n1=float(input("Enter 1st number: "))
n2=float(input("Enter 2nd number: "))
n3=float(input("Enter 3rd number: "))
if n1>=n2 and n1>=n3:
    max=n1
elif n2>=n1 and n2>=n3:
    max=n2
else:
    max=n3
print(f"Largest number is {max}")
'''
# ------------------------------------------------------

# 3rd Method
'''
n=[]
n.append(float(input("Enter 1st number: ")))
n.append(float(input("Enter 2nd number: ")))
n.append(float(input("Enter 3rd number: ")))
max=max(n)
print(f"Max number is {max}")
'''
# -----------------------------------------------------

# 4th Method
n=[]
n.append(float(input("Enter 1st number: ")))
n.append(float(input("Enter 2nd number: ")))
n.append(float(input("Enter 3rd number: ")))
sort=sorted(n)
max=sort[-1]
print(f"Max number is {max}")