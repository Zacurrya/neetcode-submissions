class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        i = 0
        res = ""
        while True:
            if i == len(strs[0]): return res

            match = strs[0][0:i+1]
            for s in strs:
               if s[0:i+1] != match:
                return res
            res = match
            i += 1
            
        return res 
                