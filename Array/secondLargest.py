def secondLargest(arr, n):
    if n < 2: 
        return -1
    large = arr[0]
    # large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]  # Array of elements
    n = len(arr)  # Size of the array

    # Find the second smallest and second largest elements
    sL = secondLargest(arr, n)

    # Output the results
    print(f"Second largest is {sL}")