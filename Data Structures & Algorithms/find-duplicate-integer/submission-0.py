class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lenN = len(nums)

        sl = 0
        ft = 0

        while True:
            sl = nums[sl]
            ft = nums[ nums[ft] ]

            if sl == ft:
                break
        
        sl = 0

        while True:
            sl = nums[sl]
            ft = nums[ft]

            if sl == ft:
                break
        
        return sl
        