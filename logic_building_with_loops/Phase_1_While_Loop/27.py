# 27. Find the LCM (Least Common Multiple) of two given numbers.



a, b = 12, 18
x, y = a, b 

while b != 0:
    a, b = b, a % b

hcf = a
lcm = (x * y) // hcf
print(lcm)


'''
| Step  | a  | b  | a % b |
| ----- | -- | -- | ----- |
| Start | 48 | 18 | 12    |
| 1     | 18 | 12 | 6     |
| 2     | 12 | 6  | 0     |
| Stop  | 6  | 0  | —     |
'''