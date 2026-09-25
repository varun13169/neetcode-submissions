class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lenA = len(arr)
        l = 0
        r = lenA -1

        while r-l + 1 > k:
            # print("Start", r-l + 1)
            if abs( arr[l] - x ) <= abs( arr[r] - x ):
                r = r - 1
            else:
                l = l + 1
            # print("End", l - r + 1)

        
        return arr[l: r+1]

        