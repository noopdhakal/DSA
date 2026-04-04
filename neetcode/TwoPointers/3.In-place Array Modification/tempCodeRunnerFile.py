from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #list(set(nums))

        if not nums:
            return 0
        
        l = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[l]:
                l += 1
                nums[l] = nums[j]
        return l + 1
            
d = Solution()
nums = [1,1,2]
print(d.removeDuplicates(nums))