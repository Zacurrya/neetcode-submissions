class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        matching = {"(":")", "[":"]", "{":"}"}
        stack = []

        for bracket in s:
            if bracket in matching.keys():
                stack.append(matching.get(bracket)) # pushes matching bracket onto the stack
            else:
                if not stack or stack.pop() != bracket:
                    return False
        return True if len(stack) == 0 else False
                