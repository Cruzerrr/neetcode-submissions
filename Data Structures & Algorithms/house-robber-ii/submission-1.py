'''class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #So our previous reccurence is now invalid-
        #PRREVIOUS SOLUTION- SUBPROBLEMS DEFINED BY WHETHER WE ROB OR SKIP
        #IF WE ROB- WE TAKE NUMS[I] + MAX SUBPROBLEM VALUE UP TO THE POINT [I-2]
        #IF WE DONT ROB- WE HAVE MAX SUBPROBLEM VALUE UP TO POINT[I-1]
        #we have two cases of which to subproblem off of=
        

        #MY SOLUTION NOW-
        
        So after reasoning it out I have come to two conclusions
        I cant do the previous solution. I cant build off of any of the previous first houses if i dont know i can take them
        i cant choose between the last and the first two becasue i need to also decide if i take the last based off of hte second last and vontinusly last houses
        so the only option is to consider whether or not i take the first or the last hosues, and solve each sepereately
        for taking the first house, we therefore cant take the last or second house so just solve it like previously but excluding the last house and second
        for taking the last house, we cant take the first or the second last so solve from index 1 up to the second last house
        now we have our recurrences depending on that 

        
        #base case
        if len(nums)== 1:
            return (nums[0])
            
        
        #case of taking first house:
        def takefirst(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0] #dp[1] = 0
            for i in range (2, (len(nums) -1)): #dont consider second and last house since we're taking the first
                dp[i] = max(dp[i-2] + nums[i], dp[i-1]) #either rob and take nums value with dp up to 2 houses down, or take dp up to 1 house down
                #i think this line above might be wrong. i think this always makes it take dpi-2 + numsi
                #bcause this will always be a non zero number in the beginning. maybe thats okay tho for the begining

            return dp[-2] #dont take the value of the last house since we cant rob from it. 
        
        def takelast(nums):
            dp = [0] * len(nums)
            # so dp[0] is just the nums of the last house
            dp[-1] = nums[-1]
            dp[0] = nums[-1] # we cant rob first house, so we take the dp value up to the rpevious dp positon


            for i in range (1, len(nums)): #dont consider first positon, already known to be nums[-1] 
                dp[i] = max(dp[i-2] + nums[i], dp[i-1]) #either rob and take nums value with dp up to 2 houses down, or take dp up to 1 house down
                #i think this line above might be wrong. i think this always makes it take dpi-2 + numsi
                #bcause this will always be a non zero number in the beginning. maybe thats okay tho for the begining
            return dp[-1] #take the last value dp 


        #return the best of the two cases
        return max(takefirst(nums), takelast(nums))
        '''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) <=3:
            return max(nums)
 
        # case 1: exclude last house
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        # case 2: exclude first house
        dp2 = [0] * (len(nums) - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])

        return max(dp1[-1], dp2[-1])
