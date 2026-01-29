# Calculate and print the factorial of every number from 1 to n.

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
    print(fact)