class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        if digits[l-1] < 9:
            digits[l-1]+=1
        else:
            for l in range(len(digits) - 1, -1, -1):
                if digits[l] < 9:
                    digits[l]+=1
                    return digits
                else:
                    digits[l]=0
            digits.insert(0, 1)
        return digits
                