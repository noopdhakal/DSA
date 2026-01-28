## Reverse the given number and print the reversed value. 

# 1234 ---> 4321


rev = 0
n = 1234
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
