class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#': #FINDING THE LENGTH
                j += 1
            length = int(s[i:j]) #CASTING LENGTH TO AN INT
            word = s[j + 1 : j + 1 + length] #WORD IS EVERYTHING AFTER # (length)
            result.append(word)
            i = j + 1 + length #MOVE START TO AFTER THE WORD JUST SAVED
        return result

