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

d = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(d.groupAnagrams(strs))