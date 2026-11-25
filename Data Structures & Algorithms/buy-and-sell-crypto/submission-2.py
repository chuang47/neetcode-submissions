class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        currMin=math.inf

        for i in range(len(prices)):
            if prices[i]<currMin:
                currMin=prices[i]
            maximum=max(maximum, prices[i]-currMin)
        return maximum