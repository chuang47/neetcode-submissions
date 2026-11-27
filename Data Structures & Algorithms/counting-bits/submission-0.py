class Solution:
    def countBits(self, n: int) -> List[int]:
        toRet = []

        for i in range(n+1):
            count = 0
            while i:
                i &= (i - 1)
                count += 1
            toRet.append(count)
        return toRet
