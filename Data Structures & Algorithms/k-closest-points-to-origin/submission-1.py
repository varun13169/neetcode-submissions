from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lenP = len(points)
        pq = PriorityQueue()


        for i in range(lenP):
            point = points[i]
            # one can use ** 0.5
            # Or doesnt need to even sqrt because here it doenst matter, sq will result in same priority
            distFromOrigin = math.sqrt( point[0]**(2) + point[1]**(2) )
            pq.put([distFromOrigin, i, point])
        
        res = []
        for i in range(k):
            point = pq.get()[2]
            res.append(point)
        
        return res


        