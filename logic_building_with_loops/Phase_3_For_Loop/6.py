# 6. Calculate and print the factorial of a given number. 

num = 5 ## 5 * 4 * 3 * 2 * 1
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(fact)