class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenS = len(s)
        lenT = len(t)
        if lenT > lenS:
            return ""

        tCharCount = {}
        for i in range(lenT):
            tCharCount[ t[i] ] = tCharCount.get(t[i], 0) + 1
        
        le = 0
        ri = 0
        resIdxs = [-1, -1]
        resLen = float('inf')

        sCharCount = {}
        have = 0

        while ri < lenS:
            sChar = s[ri]
            sCharCount[ s[ri] ] = sCharCount.get(s[ri], 0) + 1

            if sCharCount[ s[ri] ] == tCharCount.get(s[ri], -1):
                have = have + 1
            
            # print(have, tCharCount, sCharCount)
            
            while have == len(tCharCount.keys()):
                # capture res idx and res len
                if resLen >= ri - le + 1:
                    resLen = ri - le + 1
                    resIdxs = [le, ri]

                sCharToRemove = s[le]
                sCharCount[ sCharToRemove ] = sCharCount[sCharToRemove] - 1

                if sCharCount[ sCharToRemove ] < tCharCount.get(sCharToRemove, -1):
                    have = have - 1 
                le = le + 1

            ri = ri + 1


        if resLen == float('inf'):
            print(resLen)
            return ""
        
        return s[resIdxs[0]: resIdxs[1]+1]
            





        

