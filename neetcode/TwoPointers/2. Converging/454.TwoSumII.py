from collections import Counter

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = Counter()
        
        # Step 1: store sums of nums1 + nums2
        for a in nums1:
            for b in nums2:
                count[a + b] += 1
        
        # Step 2: find complementary sums
        res = 0
        for c in nums3:
            for d in nums4:
                res += count[-(c + d)]
        
        return res