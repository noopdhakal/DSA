from typing import List
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s) # immutable 
        n = len(s)
        
        for start in range(0, n, 2*k):

            left = start
            right = min(start + k - 1, n - 1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
        
s = "abcdefg"
k = 2
d = Solution()
print(d.reverseStr(s, k))