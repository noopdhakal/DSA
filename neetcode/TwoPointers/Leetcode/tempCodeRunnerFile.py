from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        print(nums[:len(unique)] )
        return unique
d= Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(d.removeDuplicates(nums))