# Write a Python program to check whether a given number is a Disarium number or not.
# (A number is called a Disarium number if the sum of its digits powered with their respective positions is equal to the number itself. e.g- 135 = 1^1+3^2+5^3=135)


num=int(input("Enter a number: "))
temp=num
count=len(str(num))
total=0
for i ,digit in enumerate(str(num),start=1):
    total=total + int(digit)**i
if total==num:
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Discrium number.")

