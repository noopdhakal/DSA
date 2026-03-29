
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        '''
        Brute Force Method
        res = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                res = max(res, min(height[i], height[j])*(j-i))
        return res
        '''
        
        # Two Pointer Method

        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            width = r - l
            area =  h * width
            res = max(res, area)


            if height[l] < height[r]:
                l +=1 
            else:
                r -= 1
            
        return res

height = [1,8,6,2,5,4,8,3,7]
d = Solution()
print(d.maxArea(height))