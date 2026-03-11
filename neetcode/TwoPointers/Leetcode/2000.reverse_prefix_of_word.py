class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        indx = word.find(ch)
        l, r = 0, indx
        if indx == -1:
            return word
        
        word = list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l+=1
            r-=1
        return "".join(word)


word = "abcdefd"
ch = "d"
d = Solution()
print(d.reversePrefix(word, ch))