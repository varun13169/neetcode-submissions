class Solution:
    def jump(self, nums: List[int]) -> int:
        lenN = len(nums)
        fathest = 0
        curJump = 0
        res = 0

        for i in range(lenN-1):
            fathest = max(fathest, i + nums[i])

            if curJump == i:
                res = res + 1
                curJump = fathest
        
        return res



        