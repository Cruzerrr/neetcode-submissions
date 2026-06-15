class Solution:
    def isPalindrome(self, s: str) -> bool:

        #convert string, strip of all non alphanumerics. 
        #check if even or odd length string
        #if even, then work from ends inwards, check if equivalent, the second it isnt then return false
        #if odd, start from middle. check going outwards if equivalent
        
        #since case insensitive:
        cleaned = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
