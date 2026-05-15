from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n-k+1): # number of subarrays 7- 3 + 1 = 5
            window = nums[i:i+k]
            print(window)
            valid = True
            for j in range(i, i + k - 1):
                if nums[j+1] != nums[j] + 1:
                    valid = False
                    break
            if valid:
                result.append(window[-1])  # maximum element
            else:
                result.append(-1)
        return result

d = Solution()
nums = [1,2,3,4,3,2,5]
k = 3
print(d.resultsArray(nums, k))
