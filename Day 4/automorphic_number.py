# Write a program to check whether a given number is an Automorphic Number or not.

# Definition: An Automorphic Number is a number whose square ends with the number itself.

# Example - 25 is an Automorphic Number because 25^2=625, which ends with 25.(76 also automorphic)

def auto(num):
    sq=str(num**2)
    num_str=str(num)
    return sq.endswith(num_str)
n=int(input("Enter a number: "))
if auto(n):
    print(f"{n} is an automorphic number.")
else:
    print(f"{n} is not a automorphic number.")