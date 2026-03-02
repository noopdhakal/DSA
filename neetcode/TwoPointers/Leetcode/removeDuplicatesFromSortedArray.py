from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
    
    # Two Pointer Method
    def removeDuplicatesTwo(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
            r += 1
        return l

d= Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(d.removeDuplicates(nums))
print(d.removeDuplicatesTwo(nums))