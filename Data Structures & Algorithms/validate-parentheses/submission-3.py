class Solution:
    def isValid(self, s: str) -> bool:
        seen=[]
        for char in s:
            if char=='[' or char=='(' or char=='{':
                seen.append(char)
            else:
                if not seen:
                    return False
                c=seen.pop()
                if c == '[' and char != ']' or c == '{' and char != '}' or c == '(' and char != ')':
                    return False

        return not seen