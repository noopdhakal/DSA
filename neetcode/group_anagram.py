from typing import List
from collections import defaultdict
class Solution:

    ## Sort Method
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for n in strs:
            key = "".join(sorted(n))
            groups[key].append(n)
        return list(groups.values())
    
    def sortAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for c in n:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(n)
        return list(res.values())

d = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(d.groupAnagrams(strs))
print(d.sortAnagrams(strs))