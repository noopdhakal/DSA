## 16. Check whether the given number is a Perfect number. 

### 6 --> divisor 1, 2, 3 then sum = 6
## Also --> 28 --> 1, 2, 4, 7, 14 if we sum then we get 28


n = 28
sum, i = 0, 1
while ( i < n):
    if n % i == 0:
        sum += i
    i += 1
print(sum)
