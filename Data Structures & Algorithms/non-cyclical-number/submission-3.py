class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False
    def sumOfSquares(self, n):
        summ = 0
        while n != 0:
            
            digit = n % 10
            digit = digit ** 2
            summ += digit
            n = n // 10
        
        return summ