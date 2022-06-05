class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(1)
        for i in range(n-1):
            dp.append(dp[i] + dp[i+1])
            
        return dp[-1]