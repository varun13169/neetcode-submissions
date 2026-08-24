class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        lenA = len(arr)
        sol = 1
        startIdx = 0

        for i in range(1, lenA):
            compPrev = self.compare(arr[i-1], arr[i])
            if compPrev == 0:
                startIdx = i
            else:
                # calc length for breakage
                if i == lenA-1 or compPrev == self.compare(arr[i], arr[i+1]) or self.compare(arr[i], arr[i+1]) == 0:
                    localSol = i - startIdx + 1
                    startIdx = i
                    sol = max(sol, localSol)

        return sol


    
    def compare(self, x, y):
        if x > y:
            return -1
        if x < y:
            return +1
        if x == y:
            return 0
        