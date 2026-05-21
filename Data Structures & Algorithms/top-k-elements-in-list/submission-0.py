class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #make each num a key in the dict
        #if found, increase count
        #if not found previously count =1
        #sort dict by counts
        #take last k items in sorted dict as a list

        found = {}
        for item in nums:
            if item not in found:
                found[item] = 1
            else:
                #it already has been found/exists, increment count
                found[item] += 1
        sortedList = sorted(found, key = lambda x: found[x]) #sort keys by their values. found[x]. lambda is one liner funciton
        output = []
        for i in range (1, k+1):
            output.append(sortedList[-i]) #recall lists uses append
        return output
            