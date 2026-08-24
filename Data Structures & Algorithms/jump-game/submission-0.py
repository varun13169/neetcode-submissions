class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lenN = len(nums)
        fartest = 0

        for i in range(lenN):
            if fartest < i:
                return False
            fartest = max(fartest, i + nums[i])
        
        return True
        