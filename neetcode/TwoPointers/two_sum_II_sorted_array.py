from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Brute Force Method
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return
    
        # Binary Search
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m 
        return -1 # not find the solution




numbers, target = [1,2,3,4], 3
d = Solution()
print(d.twoSum(numbers, target))
print(d.search(numbers, target))