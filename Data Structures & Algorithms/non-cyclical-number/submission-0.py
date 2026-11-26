class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            tmp=n
            sum=0
            while tmp != 0:
                sum+=(tmp%10)**2
                tmp//=10
            n=sum
        return n == 1