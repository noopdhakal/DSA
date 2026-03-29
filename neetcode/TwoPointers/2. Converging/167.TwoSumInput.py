from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        ## Brute Force Method
        for i in range(len(numbers)):
            for j in range(1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
        return []
        '''

        # Two pointer method

        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l, r]
        return []

numbers = [2,7,11,15]
target = 9
d = Solution()
print(d.twoSum(numbers, target))