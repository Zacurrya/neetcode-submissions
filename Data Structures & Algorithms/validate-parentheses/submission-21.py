class Solution:
    def isValid(self, s: str) -> bool:
        # edge cases
        if len(s) % 2 == 1: return False
        if len(s) == "": return True

        matching = {'{':'}', '[':']', '(':')'}
        stack = []

        for bracket in s:
            
            # opening bracket -> push matching closing brackets
            if bracket in matching.keys():    
                stack.append(matching.get(bracket))
            
            # closing bracket -> check that order is right
            else:
                if len(stack) == 0 or stack.pop() != bracket:
                    return False

        return True if len(stack) == 0 else False