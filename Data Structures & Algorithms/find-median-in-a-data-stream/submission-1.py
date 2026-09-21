from queue import PriorityQueue
class MedianFinder:

    def __init__(self):
        self.minPQ = PriorityQueue() # Upper Half
        self.maxPQ = PriorityQueue() # Lower Half
        

    def addNum(self, num: int) -> None:
        if self.minPQ.qsize() != 0:
            top = self.minPQ.get()
            if num > top:
                self.minPQ.put(num)
            else:
                self.maxPQ.put(-1 * num)
            self.minPQ.put(top)
        else:
            self.maxPQ.put(-1 * num)
        
        while self.minPQ.qsize() - self.maxPQ.qsize() > 1:
            self.maxPQ.put( -1 * self.minPQ.get() )
        while self.maxPQ.qsize() - self.minPQ.qsize() > 1:
            self.minPQ.put( -1 * self.maxPQ.get() )


    def findMedian(self) -> float:
        if self.minPQ.qsize() == self.maxPQ.qsize():
            minTop = self.minPQ.get()
            maxTop = self.maxPQ.get()
            self.minPQ.put(minTop)
            self.maxPQ.put(maxTop)

            res = ( minTop + (-1*maxTop) ) / 2
            return res
        else:
            if self.minPQ.qsize() > self.maxPQ.qsize():
                minTop = self.minPQ.get()
                self.minPQ.put(minTop)
                return minTop
            
            if self.maxPQ.qsize() > self.minPQ.qsize():
                maxTop = self.maxPQ.get()
                self.maxPQ.put(maxTop)
                return -1 * maxTop

            


        
        