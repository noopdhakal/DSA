from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # i = 0
        # for num in nums2:
        #     if nums1[num] == num:
        #         print(num)


        return list(set(nums1) & set(nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
d = Solution()
print(d.intersection(nums1, nums2))
