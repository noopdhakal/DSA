from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # brute force method

        # for i in range(len(nums1)):
        #     return -1
        number_1 =  nums1[:-m]
        number_2 = nums2[:-n]
        return sorted(nums1[:m] + nums2[:n])

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
d = Solution()
print(d.merge(nums1, 3, nums2, 3))