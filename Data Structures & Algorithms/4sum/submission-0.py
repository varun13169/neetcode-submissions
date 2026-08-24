class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lenN = len(nums)
        res = set([])

        for i in range(lenN):
            for j in range(i+1, lenN):
                newTarget = target - nums[i] - nums[j]

                twoSumRes = []
                self.twoSum(j+1, lenN-1, nums, twoSumRes, newTarget)
                
                for tS in twoSumRes:
                    res.add( tuple(sorted((nums[i], nums[j], tS[0], tS[1]))) )
        
        return list(res)

        




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
            i = i + 1

        