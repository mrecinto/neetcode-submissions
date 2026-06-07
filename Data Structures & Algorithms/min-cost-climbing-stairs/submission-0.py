class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       # return the minimum cost to reach the top
       # you can either take 1 or 2 steps

       # recurrence would be
       # dp[i] = min cost it took to reach that step?
       # so dp[i] would depend on the min cost of the previous?

       # base cases would be 
       # starting step. dp[0] = 0, dp[1] = 0

       # find the minimum of the array
       n = len(cost)
       dp = [0] * (n+1)

       dp[0] = 0
       dp[1] = 0

       for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

       return dp[n]
