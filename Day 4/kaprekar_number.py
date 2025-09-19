# Write a program to check whether a given number is a Kaprekar Number or not.

# Definition: A Kaprekar Number is a number whose square can be split into two parts that add up to the original number. For example, 45 is a Kaprekar Number because:
# e.g - 45**2=2025 ⇒ 20+25=45

def kap(num):
    if num==1:
        return True
    sq=str(num**2)
    length=len(sq)

    for i in range (1,length):
        left=int(sq[:i]) if sq[:i] else 0
        right=int(sq[i:]) if sq[i:] else 0

        if right>0 and (left+right)==num:
            return True
    return False

n= int(input("Enter a number: "))
if kap(n):
    print(f"{n} is a Kaprekar number.")
else:
    print(f"{n} is not a Kaprekar number.")