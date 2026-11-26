class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            tmp=n
            sum=0
            while tmp != 0:
                sum+=(tmp%10)**2
                tmp//=10
            n=sum

            if n==1:
                return True
        return n == 1