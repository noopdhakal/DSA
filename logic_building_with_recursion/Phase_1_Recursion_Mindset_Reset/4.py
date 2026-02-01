#  Print "Before Call" and "After Call" to observe call order. 


def observer(n):
    if n == 0:
        return
    print("Before Call", n)
    observer(n-1)
    print("After Call", n)

observer(3)