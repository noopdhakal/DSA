from typing import List, Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n-k+1):
            window = nums[i:i+k]

            freq = Counter(window)

            # sort
            sorted_items = sorted(

                freq.items(),
                key = lambda item: (-item[1], -item[0])
            )
            
            top_x = sorted_items[:x]

            total = 0
            for num, count in top_x:
                total += num * count
        
        
            result.append(total)


        return result
   
d = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
print(d.findXSum(nums, k, x))