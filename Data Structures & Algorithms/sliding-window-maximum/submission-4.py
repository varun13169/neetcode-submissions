class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenN = len(nums)
        maxEleIdxQ = deque()
        res = []

        # maxIdxTillK = 0
        # for i in range(k):
        #     if nums[maxIdxTillK] < nums[i]:
        #         maxIdxTillK = i
        
        # maxEleIdxQ.append(maxIdxTillK)
        # res.append( nums[ maxIdxTillK ] )
        
        for i in range(0, lenN):
            while len(maxEleIdxQ) != 0 and maxEleIdxQ[0] <= i - k:
                maxEleIdxQ.popleft()

            while len(maxEleIdxQ) != 0 and nums[ maxEleIdxQ[-1] ] < nums[i]:
                maxEleIdxQ.pop()

            maxEleIdxQ.append( i )

            if i >= k-1:
                res.append( nums[ maxEleIdxQ[0] ] )

        return res
            


            
