class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenN = len(nums)
        q = deque() # most outdated node ........ most recent node
        le = 0
        ri = 0
        res = []

        while ri < lenN:
            # clear all smaller elements before ri (latest) element index
            while len(q) != 0 and nums[ri] >= nums[ q[-1] ]:
                q.pop() # pop(-1)
            # append the latest element index
            q.append(ri)

            # clear indexes which is out of window
            if le > q[0]:
                q.popleft() # pop(0)

            # capture window
            if ri - le + 1 >= k:
                curLargestEle = nums[ q[0] ]
                res.append( curLargestEle )
                le = le + 1
            ri = ri + 1
        
        return res
        