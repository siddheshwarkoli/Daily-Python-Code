# Write a Python program that asks the user to input a number and checks whether the number is a palindrome.

# 1st Method
'''
num=int(input("Enter a number: "))
if str(num)==str(num)[::-1]:
    print(num," is palindrome number.")
else:
    print(num," is not a palindrome number.")
'''
# ----------------------------------------------------

# 2nd Method
'''
num=int(input("Enter a number: "))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print(original," is palindrome number.")
else:
    print(original," is not a palindrome number.")
'''
# --------------------------------------------------

# 3rd Method
'''
def pali(num):
    return str(num)==str(num)[::-1]
num=int(input("Enter a number: "))
if pali(num):
    print(num," is palindrome number.")
else:
    print(num," is not a palindrome number.")
'''
# ------------------------------------------------

# 4th Method
def pali(num):
    original=num
    reverse=0
    while num>0:
        reverse = reverse *10+(num%10)
        num =num//10
    return original==reverse
num=int(input("Enter a number: "))
if pali(num):
    print(num," is palindrome number.")
else:
    print(num," is not a palindrome number.")
