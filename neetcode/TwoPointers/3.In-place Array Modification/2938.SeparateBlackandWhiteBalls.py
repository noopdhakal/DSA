class Solution:
    def minimumSteps(self, s: str) -> int:
        # l = 0
        # s = list(s)
        # for i in range(1, len(s)):
        #     if s[l] > s[i]:
        #         s[l], s[i] = s[i], s[l]
        #         l += 1
        #         i += 1
        # return l

        steps = 0 
        zero_count = 0 

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                zero_count += 1
            else:
                steps += zero_count
        return steps

s = "11000111"
d = Solution()
print(d.minimumSteps(s))