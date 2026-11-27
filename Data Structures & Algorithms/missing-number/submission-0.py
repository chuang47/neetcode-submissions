class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for n in range(len(nums)):
            sum += nums[n]
        return (len(nums) * (len(nums) + 1) // 2) - sum