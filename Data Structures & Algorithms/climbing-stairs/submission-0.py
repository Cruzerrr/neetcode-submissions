class Solution:
    def climbStairs(self, n: int) -> int:
        
        #total ways given by the following strucutre
        #last step - 1 + all the ways to get there on the smaller subproblem
        #last step - 2 + ""

        #so its like fibonacci. current step depends on the two ways previous to it that bring it there

        #base case ways to get to step1/2

        #ways to 0 and 1 are just 1. do nothing is still a way to get there
        ways1 = 1
        ways2 = 1
        for i in range(n-1):
            temp = ways1
            ways1 = ways1 + ways2
            ways2= temp
        return ways1

        