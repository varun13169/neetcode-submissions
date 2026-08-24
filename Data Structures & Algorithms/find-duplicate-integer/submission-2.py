class Solution:
    def findDuplicate_withIdx0(self, nums: List[int]) -> int:
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
            if sl == ft:
                break
            sl = nums[sl]
            ft = nums[ft]

        return sl
        
    def findDuplicate(self, nums: List[int]) -> int:
        lenN = len(nums)

        sl = nums[0]
        ft = nums[0]

        while True:
            sl = nums[sl]
            ft = nums[ nums[ft] ]

            if sl == ft:
                break
        
        sl = nums[0]
        while True:
            if sl == ft:
                break
            sl = nums[sl]
            ft = nums[ft]

        
        return sl
        