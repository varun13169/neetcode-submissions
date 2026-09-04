class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        lenN = len(nums)

        res = []
        i = 0
        while i < k:
            while len(dq) != 0 and dq[len(dq)-1][1] < nums[i]:
                dq.pop()
            dq.append([i, nums[i]])
            i = i + 1
        
        res.append(dq[0][1])

        while i < lenN:
            ele = nums[i]

            # remove if exiting idx is present from left
            validIdx = i - k + 1
            while len(dq) != 0 and dq[0][0] < validIdx:
                dq.popleft()
            ##################

            while len(dq) != 0 and dq[len(dq)-1][1] < nums[i]:
                dq.pop()
            dq.append([i, nums[i]])

            res.append(dq[0][1])
            i = i + 1

        
        return res
        