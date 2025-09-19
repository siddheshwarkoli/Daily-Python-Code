# Write a program to check whether a given number is a Spy Number or not.

# Definition: A Spy Number is a number where the sum of its digits is equal to the product of its digits.

# Example : 1124 is a Spy Number because:
#           Sum of digits = 1+1+2+4 = 8
#           Product of digit = 1x1x2x4=8

def spy(num):
    digit=[int(d) for d in str(num)]
    t_sum=sum(digit)
    t_product=1
    for d in digit:
        t_product=t_product*d
    return t_sum==t_product

n=int(input("Enter a number: "))
if spy(n):
    print(f"{n} is a Spy number.")
else:
    print(f"{n} is not a Spy number.")