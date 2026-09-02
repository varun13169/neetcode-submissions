class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lenN = len(nums)
        res = []

        for i in range(lenN):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print(i)
            for j in range(i+1, lenN):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # print(j)
                newTarget = target - nums[i] - nums[j]

                twoSumRes = []
                self.twoSum(j+1, lenN-1, nums, twoSumRes, newTarget)
                
                for tS in twoSumRes:
                    res.append( (nums[i], nums[j], tS[0], tS[1]) )
        
        return res

        




    def twoSum(self, st, ed, nums, twoSumRes, target):
        diffMap = {}

        i = st
        while i <= ed:
            # print(i, ed, len(nums))
            if diffMap.get(nums[i], "None") == "None":
                diff = target - nums[i]
                diffMap[diff] = nums[i]
            else:
                # diffMap[nums[i]] valuse of this would have come first
                twoSumRes.append([diffMap[nums[i]], nums[i]])
                while i+1 <= ed and nums[i] == nums[i+1]:
                    i = i + 1
            i = i + 1

        