class Solution:
    def rob(self, nums: List[int]) -> int:
       # cannot rob two adjacent houses
       # x = skip * = rob
       # * x * x * x
       # x * x * x *
       # x * x x * x not always every other house
       n = len(nums)
       if n == 1:
        return nums[0]
    
       D = [0]*(n)
       # base cases: 
       # only one house, rob it
       D[0] = nums[0]
       # two houses, then decide if 
       D[1] = max(nums[0], nums[1])
       if n == 2:
        return D[1]

       # recurrence
       #this boils down to 2 decisions: to skip or to rob
       # skip = D[i-1]

       # rob = nums[i] + D[i-2]
       # in words this is saying, take the current one, then add up the
       # sequence before the previous one since adjacents are an issue

       # D[i] = max money at ith house=  IN vs OUT= max(IN(rob),OUT(skip))
       for i in range(2, n):
        skip = D[i-1]
        rob = nums[i] + D[i-2]
        D[i]= max(skip,rob)
       return D[n-1]