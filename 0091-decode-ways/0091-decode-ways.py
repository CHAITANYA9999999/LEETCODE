class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, n):
            if s[i] != "0":
                dp[i + 1] = dp[i]
            if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6"):
                dp[i + 1] += dp[i - 1]

        return dp[n]
