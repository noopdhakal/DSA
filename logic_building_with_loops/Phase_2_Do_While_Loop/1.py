# Print all numbers from 1 to 10. 

# Python has no do-while, but while True + break behaves exactly the same.

i = 1 
while True:
    print(i)
    i += 1

    if i > 10:
        break