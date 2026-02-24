from typing import List
class Solution:

    ## Brute Force Method
    def twoSum(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                

    def hashMap(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

d = Solution()
nums, target = [3, 4, 5, 6], 7 
# print(d.twoSum(nums, target))
# print(d.twoSum([4,5,6], 10))
print(d.hashMap(nums, target))