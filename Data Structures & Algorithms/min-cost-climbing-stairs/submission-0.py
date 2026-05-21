class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #optimal solution is:
        #from top, best step from -1 or -2 . and the subproblem considered from beginning to that new best step
        #therefore 
        #opt = [minimalstepcost(top) + subproblem rest of staircase] 
        '''
        n = len(cost)
        solution = min(cost[i-1] + minCostClimbiingStairs(cost.pop(), cost[i-2] + minCostClimbingStairs()))

        #'''
        #DIDNT REALIZE I CAN STATART AT FLOOR 0 OR 1

        n = len(cost)
        dp = [0] * n  #init 1d 0 cost

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range (2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1],dp[-2]) #which second last step brings the best


        