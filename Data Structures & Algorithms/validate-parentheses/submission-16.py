class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        brackets = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in brackets.keys():
                stack.append(brackets.get(c))
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False