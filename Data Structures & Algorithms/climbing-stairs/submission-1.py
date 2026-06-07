class Solution:
    def climbStairs(self, n: int) -> int:

        # n = 5
        # 0,1,2,3,4,5
        dp = [0]*(n+1)

        # base cases:
        # n = 0, there is 1 way to reach 0? by taking no steps?
        # if the solution doesnt care then dp[0]=0
        # n = 1, there is 1 step to reach 1 step
        # n = 2, you can either take 1 step or 2 step
        # so: 1 + 1, 0 + 2
        # dp[n] = steps it took to get 1 before (i-1) + steps it took to get 2 before (i-2)

        #ordering of subproblems, you want to go from left to right since each consecutive step
        # depends on the previous ones

        if n == 1: return 1
        if n == 2: return 2
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]