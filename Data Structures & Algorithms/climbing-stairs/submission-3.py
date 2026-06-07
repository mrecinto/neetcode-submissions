class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases:
        # when youre at the first/second step
        if n == 1: return 1
        if n == 2: return 2
        D = [0]*(n+1)
        D[0] = 0
        D[1] = 1
        D[2] = 2

        # there are 2 decisions u can make, go 1 step or 2
        for i in range(3,n+1):
            # D[i] = number of ways for the i'th step
            #      = 1-step back + 2-step back
            D[i] = D[i-1] + D[i-2]

        return D[n]
        