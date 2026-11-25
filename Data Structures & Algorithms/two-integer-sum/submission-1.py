class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toRet=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    toRet.append(i)
                    toRet.append(j)
                    return toRet
        return toRet