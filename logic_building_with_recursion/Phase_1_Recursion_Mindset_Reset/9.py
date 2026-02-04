#  Write a recursive function that stops only when n == 0.

def recur_stop(n):
    if n == 0:
        print("Stopped")
        return
    recur_stop(n-1)

recur_stop(10)