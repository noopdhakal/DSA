# from typing import list
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       i = 0
       for char in t:
           if i < len(s) and s[i] == char:
               i += 1
       return i == len(s)

        

d = Solution()
print(d.isSubsequence("abc", "ahbgdc"))