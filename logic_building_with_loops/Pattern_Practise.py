n = 5
print("*" * n)

for j in range(n):
    print("*", end='')


for i in range(n):
    for j in range(n):
        print("*", end='')

for i in range(n):
    for j in range(n):
        print("*", end=' ') ## print column wise
    print()


    #  i = 0 * * * * *
    # print() and goes to next line exiting the outer 

## Increasing Triangle 
for i in range(n): ## outer row is fine 
    for j in range(i + 1):
        print("*", end=' ') ## print column wise
    print()

"""
i=0    *            here only + 1 in j column same as other
i=1    * *
i=2    * * *
i=3    * * * *
i=4    * * * * *

"""

print("\n")

## Decresing Triangle 
for i in range(n): ## outer row is fine 
    for j in range(i,n):
        print("*", end=' ') ## print column wise
    print()

# 0 to 5
# 1 to 5
# 2 to 5
# 3 to 5
# 4 to 5

# * * * * * 
# * * * * 
# * * * 
# * * 
# *


## Different types of patterns

'''
1. Right Triangle  --- A. Decreasing traingle of Space, Increasing Triangle of Star
2. Left Traingle   --- A. Increasing traingle of Space, Decreasing Traingle fo Star
3. Hill Pattern    --- A. Three Patterns, Decreasing Pattern of space, Increasing traingle of star, Increasing traingle of star
4. Reverse Hill     
'''

# 1. Right Triangle

for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print('*', end=" ")
    print()
'''
          * 
        * * 
      * * * 
    * * * * 
  * * * * *
'''
print('\n')
# 2. Left Triangle

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print('*', end=" ")
    print() 

#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           * 

# 3. Hill Pattern

print("\n")
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

## 4. Reverse Hill Pattern

print("\n")
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n-1): ## for one less column
        print("C", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

## 5 Diamond Star Pattern

print("\n")
for i in range(n-1): ## outer loop reducing by so it can be pointed
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n-1): ## for one less column
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


## Reference: https://www.youtube.com/watch?v=fX64q6sYom0