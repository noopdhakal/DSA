# Count and print the total number of digits in a given number. 

n = 1245
count = 0
if n == 0:
    count = 1
else: 
    while ( n > 0):
        count += 1
        n //= 10
print(count)