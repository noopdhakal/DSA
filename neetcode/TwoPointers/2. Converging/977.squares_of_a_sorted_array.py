from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # sortValue = []
        # for num in nums:
        #     sortValue.append(num**2)
        # return sorted(sortValue)

        n = len(nums)
        result = [0] * n
        pos = n - 1

        l, r = 0, n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] ** 2
                l+=1
            else:
                result[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return result
            
            


        
s = [-4,-1,0,3,10]
d = Solution()
print(d.sortedSquares(s))