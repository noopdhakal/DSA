 # Find and print the product of all digits of a given number. 

n = 123
prod = 1
while ( n > 0):
    prod *= n % 10
    n //= 10 ## returns 12 only

print(prod)