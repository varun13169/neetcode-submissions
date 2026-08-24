class Solution:
    def trap(self, height: List[int]) -> int:
        lenH = len(height)
        le = 0
        ri = lenH-1
        leMax = height[le]
        riMax = height[ri]
        res = 0

        while le <= ri:
            if height[le] < height[ri]:
                # do something
                leMax = max(leMax, height[le])
                res = res + (leMax - height[le])
                le = le + 1
            else:
                # do something else
                riMax = max(riMax, height[ri])
                res = res + (riMax - height[ri])
                ri = ri - 1
        
        return res