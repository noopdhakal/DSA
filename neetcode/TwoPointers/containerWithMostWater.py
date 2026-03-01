from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force

        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        return res
    
        ## Two Pointer Method 

    def maxArea_1(self, heights: List[int]) -> int:
        # brute force
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res



height = [1,7,2,5,4,7,3,6]
d = Solution()
print(d.maxArea(height))
print(d.maxArea_1(height))