class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []

        for char in s:
            if char in opening: # checks if it's a bracket
                stack.append(opening[char]) # push expected closing bracket
            elif not stack or stack.pop() != char: 
                return False
        
        return not stack # true if empty