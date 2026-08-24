class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS == 0:
            return 0

        maxxLen = 1
        sol = s[0]
        for i in range(lenS):
            center = s[i]
            localLen = 1

            # Odd
            st = i
            ed = i
            while st >= 0 and ed < lenS and s[st] == s[ed]:
                localLen = ed - st + 1
                if maxxLen < localLen:
                    maxxLen = localLen
                    sol = s[st: ed+1]
                st = st - 1
                ed = ed + 1

            # Even
            st = i - 1
            ed = i
            while st >= 0 and ed < lenS and s[st] == s[ed]:
                localLen = ed - st + 1
                if maxxLen < localLen:
                    maxxLen = localLen
                    sol = s[st: ed+1]
                st = st - 1
                ed = ed + 1

        return sol


        