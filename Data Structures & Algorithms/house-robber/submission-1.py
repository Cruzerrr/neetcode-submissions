class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #we need to compute a max subproblem
        #by picking greedily, we can suboptimally imit other houses.
        #to get around this, we need a recurrence pattern. 
        #cant pick greedily. pick [i-1, i+1] intervals that produce the most. ideally not picking 
        #those houses which are three away. only doing so if their 3 range interval is less than the 3rd house

         #i want the table to return the max amount. needs to thus be 1d , using indices

         #definf dp table to be the max amount that i can get up to house i:
         #if i rob house i: the max i can get is up to house i-2 plus the number at the house
         #this is because i cant take house i-1 num because it would set off the alarm

         #if i skip house i: the max i can get is up to house i-1 since i didnt rob current house and house i-1 is possible to take
        # so dp reccurrence then becomes:  dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp = [0] * len(nums) #initialize table 
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0] #max we can take at the beginning is just what we have at the beginnign
        dp[1] = max(nums[0], nums[1] )#max we can take at second place is the better of the two options
        for i in range (2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

        #what am i missing:
        #need to return last dp entry since it is just the max i can take ,
        #need to set up base cases: dont be silly





            
                