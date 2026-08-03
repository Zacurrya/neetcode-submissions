class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = {} # num : frequency

        # map num : freq to count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # add pairs to the frequency array    
        for num, frequency in count.items():
            freq[frequency].append(num)

        res = []
        # traverse freq backwards, adding most frequent elements to top_k array
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
