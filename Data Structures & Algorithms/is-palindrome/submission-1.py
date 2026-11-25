class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char for char in s if char.isalnum())
        cleaned=s.lower()
        return cleaned==cleaned[::-1]
        