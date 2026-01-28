#  Check whether the given number is a palindrome. 

# 121, 1331, 7 these all are the palindrome number

n = int(input("You'r Number Please"))
original, rev = n, 0
while (n > 0):
    rev = rev * 10 + n % 10
    n //= 10
# print(n, rev)
if original == rev:
    print('It''s Palindrome number')
else:
    print('No Palindrome number')
# print(rev)
