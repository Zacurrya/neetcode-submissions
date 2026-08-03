class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            diff = target-num
            if diff in map.keys():
                return [map.get(diff), i]
            else:
                map[num] = i