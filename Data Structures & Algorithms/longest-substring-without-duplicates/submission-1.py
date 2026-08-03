class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        letters = set()
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            maxLen = max(maxLen, (r-l)+1)
            letters.add(s[r])

        return maxLen

            