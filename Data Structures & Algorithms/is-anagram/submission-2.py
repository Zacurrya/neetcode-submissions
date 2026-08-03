class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sm, st = {}, {}
        for i in range(len(s)):
            sm[s[i]] = 1 + sm.get(s[i], 0) 
            st[t[i]] = 1 + st.get(t[i], 0) 
        
        if sm != st:
            return False
        return True
    