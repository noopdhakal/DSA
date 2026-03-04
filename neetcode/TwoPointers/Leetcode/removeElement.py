from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] ## swap itself
                k += 1
        return k

d= Solution()
nums, val = [3,2,2,3], 3
print(d.removeElement(nums, val))