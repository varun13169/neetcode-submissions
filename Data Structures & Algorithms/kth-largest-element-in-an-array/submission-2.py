from queue import PriorityQueue

class Solution:
    # Better because of space complexity
    # Time: O(N)
    # Space: O(K)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lenN = len(nums)

        pq = PriorityQueue()

        for i in range(lenN):
            pq.put(nums[i])

            while pq.qsize()-k > 0:
                pq.get()
        
        res = []
        for i in range(k):
            res.append(pq.get())
        
        # here if the diff from below
        return res[0]

    # Time: O(N)
    # Space: O(N)
    def findKthLargest_(self, nums: List[int], k: int) -> int:
        lenN = len(nums)

        pq = PriorityQueue()

        for i in range(lenN):
            pq.put(-1 * nums[i])

        
        res = []
        for i in range(k):
            res.append(-1 * pq.get())

        # here is diff from above approach
        return res[-1]
        
        
        