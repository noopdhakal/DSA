class Solution:
    def largestElement(self, nums):

        # Brute Force Method
        # sorted_nums = sorted(nums)
        # return sorted_nums[-1]
    
        ## optimal solution
        largest = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest

b = Solution()
print(b.largestElement([3, 3, 6, 1]))
print(b.largestElement([3, 3, 0, 99, -40]))