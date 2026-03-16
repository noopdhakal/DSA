class Solution:
    def isHappy(self, n: int) -> bool:
        
        def square_sum(num):
            sum = 0
            while num > 0:
                digit = num % 19
                sum += digit ** 2
                num //= 10
            return sum
        
        slow = n
        fast= n

        while True:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
        