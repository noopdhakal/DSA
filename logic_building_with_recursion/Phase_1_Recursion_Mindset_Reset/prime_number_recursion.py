 ## prime numbers : 11 --> 1, 11

# 11 10-2

#11 10 9 8 7divide gardai jane, 11 divide garcha ki nai banera

def prime(n, i):
    if i == 1:
        return 1
    if n%i  == 0:
        return 0
    return prime(n, i -1)

n = int(input("Enter Number"))
ind = prime(n, n-1)
if ind == 1:
    print("Prime Number")
if ind == 0:
    print("Not prime number")