from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Brute Force Method
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return
    
        # Binary Search
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m 
        return -1 # not find the solution

    def Binary2Sum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            temp = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == temp:
                    return [i+1, mid+1]
                elif numbers[mid] < temp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
    
    ## Two pointers

    def twoSumPointer(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curtSum = numbers[l] + numbers[r]

            if curtSum > target:
                r -= 1
            elif curtSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


numbers, target = [1,2,3,4], 3
d = Solution()
print(d.twoSum(numbers, target))
print(d.search(numbers, target))
print(d.Binary2Sum(numbers, target))
print(d.twoSumPointer(numbers, target))