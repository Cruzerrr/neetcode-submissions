class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for item in strs:
            #sort each word
            key = tuple(sorted(item))
            if key not in anagrams: 
                anagrams[key] = []

            anagrams[key].append(item)
        return list(anagrams.values())

        




            
        