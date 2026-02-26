from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        
        res = []

        while (len(res) < k):
            res.append(arr.pop()[1])

        return res


d = Solution()
nums = [1,2,2,3,3,3]
k = 2
print(d.topKFrequent(nums, k))