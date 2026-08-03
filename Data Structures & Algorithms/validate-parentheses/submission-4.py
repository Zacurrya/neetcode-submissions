class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        elif not s:
            return True

        matching = {'[':']', '(':')', '{': '}'}
        stack = []

        for c in s:
            if c in matching.keys():
                stack.append(matching.get(c))
            else:
                if not stack or stack.pop() != c:
                    return False
        if stack:
            return False
        return True