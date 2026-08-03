class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        seen = set()
        longest = 1
        # First add to the set
        for num in nums:
            seen.add(num)
        # Then check for sequences
        for num in nums:
            length = 1
            # Not the start of a sequence
            while (num-1) in seen:
                length += 1
                num -= 1
            
            longest = max(longest, length)
        
        return longest
