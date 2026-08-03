class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {} # val : index
        
        for i, num in enumerate(nums):
            if target-num in hm: 
                return [
                    min(i, hm[target-num]), 
                    max(i, hm[target-num])
                    ]
            hm[num] = i
