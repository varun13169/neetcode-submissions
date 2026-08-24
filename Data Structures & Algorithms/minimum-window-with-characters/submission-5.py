class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenS = len(s)
        lenT = len(t)

        if lenT > lenS:
            return ""

        tCharCount = {}
        for i in range(lenT):
            tCharCount[t[i]] = tCharCount.get(t[i], 0) + 1

        have = 0
        need = len(tCharCount.keys())
        le = 0
        ri = 0
        res = [-1, -1]
        resLen = float('inf')
        sCharCount = {}

        while ri < lenS:
            char = s[ri]
            sCharCount[ char ] = sCharCount.get(char, 0) + 1
            if sCharCount[ char ] == tCharCount.get(char, 0):
                have = have + 1
            # print(have)
            
            while have == need:
                if resLen > ri - le + 1:
                    resLen = ri - le + 1
                    res = [le, ri]
                    # print(res )
                # resLen = min(resLen, ri - le + 1)

                sCharCount[ s[le] ] = sCharCount[ s[le] ] - 1
                if tCharCount.get(s[le], 0) != 0 and sCharCount[ s[le] ] < tCharCount.get(s[le], 0):
                    have = have - 1

                le = le + 1
            ri = ri + 1
        
        if resLen:
            return s[res[0]: res[1]+1]
        return ""


        