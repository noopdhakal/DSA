def secondLargest(nums):
    large, secondlarge = -1, -1
    for i in range(len(nums)):
        if nums[i] > large:
            secondlarge = large
            large = nums[i]
        elif nums[i] > secondlarge and nums[i] != large:
            secondlarge = nums[i]
    return secondlarge
        

print(secondLargest([1, 2, 4, 7, 7, 5]))