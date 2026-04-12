class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        def get_next(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10
            return total
        
        slow = n 
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
    
        return fast == 1

n = 19
d = Solution()
print(d.isHappy(n))