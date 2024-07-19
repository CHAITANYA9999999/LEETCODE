class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp=[[False for _ in range(n)] for _ in range(n)]

        count=0

        for length in range(1,n+1):
            for i in range(n-length+1):
                if s[i] == s[i+length-1] and (length<=2 or dp[i+1][i+length-2]):
                    count+=1
                    dp[i][i+length-1] = True
        return count