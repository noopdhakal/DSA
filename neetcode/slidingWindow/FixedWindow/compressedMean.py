from typing import List

class Solution:
    def compressedMean(self, nums: List[int]) -> float:
        stack = []

        for num in nums:
            if stack and stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)
        return sum(stack)/len(stack)
    
d = Solution()
nums = [1, 1, 2, 3, 3]
print(d.compressedMean(nums))