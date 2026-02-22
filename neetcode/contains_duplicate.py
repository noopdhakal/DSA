from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
d = Solution()
print(d.hasDuplicate([1, 2, 3, 3]))