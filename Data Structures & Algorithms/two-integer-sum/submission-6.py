class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, num in enumerate(nums):
            if target-num in m:
                return [min(i, m[target-num]), max(i, m[target-num])]
            
            m[num] = i

            
