from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # We only need to go to n - 2 to leave room for l and r
        for i in range(n - 2):
            # Optimization: Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # If we found the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the current_sum is nearer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum

nums = [-1,2,1,-4]
target = 1
d = Solution()
print(d.threeSumClosest(nums, target))