class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        prefixHeight = []
        tallest = 0
        for i in range(len(height)):
            tallest = max(tallest, height[i])
            prefixHeight.append(tallest)
        
        tallest = 0
        postfixHeight = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            tallest = max(tallest, height[i])
            postfixHeight[i] = tallest
        
        for i in range(1, len(height)):
            res += min(prefixHeight[i], postfixHeight[i]) - height[i]
        
        return res