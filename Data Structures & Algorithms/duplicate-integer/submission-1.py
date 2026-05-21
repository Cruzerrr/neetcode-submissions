class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        found = {}
        for i in nums:
            if i not in found:
                found[i] = True              
            else: return True
        return False