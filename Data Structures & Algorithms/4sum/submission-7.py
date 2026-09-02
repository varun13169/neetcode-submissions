class Solution:
    def fourSum_SpecificTo4Sum(self, nums: List[int], target: int) -> List[List[int]]:
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

        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lenN = len(nums)
        res = []
        tempRes = []
        self.fourSumUtil(0, lenN-1, res, tempRes, nums, target, 4)

        return res

    def fourSumUtil(self, st, ed, res, tempRes, nums, target, sumSolCount):
        # check for possible

        # if sumSolCount == 2
        if sumSolCount == 2:
            twoSumRes = []
            # print(nums)
            # print(tempRes, st, ed)
            self.twoSum(st, ed, nums, twoSumRes, target)
            for ts in twoSumRes:
                r = tempRes[:]
                r.append(ts[0])
                r.append(ts[1])
                res.append(r)
        
        else:
            for i in range(st, ed+1):
                if i > st  and nums[i] == nums[i-1]:
                    continue
                ele = nums[i]
                newTarget = target - ele
                tempRes.append(ele)
                self.fourSumUtil(i+1, ed, res, tempRes, nums, newTarget, sumSolCount-1)
                tempRes.pop()
        


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

        