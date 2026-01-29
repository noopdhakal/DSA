# write a python program for printing n to 1 sequence

## Direct Recursion
def program(n):
    if n == 0:
        return
    print(n, end=" ")
    return program(n -1)

program(10)

# def func():
#     base condn:
#         return ## stop
#     return [ recursive Calls]

## Indirect Recursion, a function calls another functionw which then calls the first function again.