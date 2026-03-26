class Solution:
    def reverseWords(self, s: str) -> str:
        s =  s.split()
        l, r = 0, len(s) - 1
        while l < r:
            # if s[l] == " ":
            #     l += 1
            # elif s[r] == " ":
            #     r -= 1
            # else:
            #     s[l], s[r] = s[r], s[l]
            #     l += 1
            #     r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return " ".join(s)

s = "  hello world  "
d = Solution()
print(d.reverseWords(s))