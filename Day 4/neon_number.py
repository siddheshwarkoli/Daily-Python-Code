# Write a program to check whether a given number is a Neon Number or not.

# Defination: A Neon Number is a number where the sum of the digits of the square of the number is equal to the number itself.

# Example : 9 is a Neon Number because:
#           9^2=81 and sum of digit=8+1=9

def neon(num):
    sq=num**2
    d_sum=sum(int(d) for d in str(sq))
    return d_sum==num
n=int(input("Enter a number: "))
if neon(n):
    print(f"{n} is a Neon number")
else:
    print(f"{n} is not a neon numbeer.")