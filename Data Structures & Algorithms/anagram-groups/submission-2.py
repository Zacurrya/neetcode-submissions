class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # default value of a list allows us to append words without needing to have any words there already

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1    
            res[tuple(count)].append(s)
        return list(res.values())