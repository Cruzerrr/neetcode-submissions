class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1 = {}
        count2 = {}
        for char in s:
            if char not in count1:
                count1[char] = 0
            count1[char] += 1
        
        for char in t:
            if char not in count2:
                count2[char] = 0
            count2[char] += 1
        
        if count1 == count2:
            return True
        else: return False


        