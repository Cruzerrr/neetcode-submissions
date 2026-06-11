class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        new = sorted(nums)
        longest = 1
        current = 1
        
        for i in range(len(nums) - 1):
            
            if new [i+1] == new[i]: #duplicates, skip, doesnt add anything
                continue
            elif (new[i + 1] - 1) == new[i]:
                current +=1
            else:
                current = 1
            longest = max(longest, current)
        return longest
            


