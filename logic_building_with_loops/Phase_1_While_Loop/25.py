# 25 Find and print the sum of all factors of the given number. 

n = 10
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i += 1 
print("The sum of all the factors is", sum)