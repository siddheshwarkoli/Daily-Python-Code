# Write a program to check whether a given number is a Happy Number or not.

#Definition: A Happy Number is a number that eventually reaches 1 when replaced by the sum of the squares of each digit repeatedly. If the process results in an endless cycle that does not include 1, the number is not a Happy Number.

def happy(num):
    seen=set()
    while num!=1 and num not in seen:
        seen.add(num)
        num=sum(int(digit)**2 for digit in str(num))
    return num==1
n=int(input("Enter a number: "))
if happy(n):
    print(f"{n} is a Happy number.")
else:
    print(f"{n} is not a Happy number.")