class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Create a set to store character
        #Whenever we saw a duplicate char, pop the left most 
        #until no dup exist
        #Constantly updating the set along with our result

        storage = set()
        l = 0
        res = 0
        for idx, val in enumerate(s):
            while val in storage:
                #Keep poping the leftmost 
                storage.remove(s[l])
                l += 1
            #if there is no dup
            storage.add(val)
            res = max(res, idx - l + 1)
        return res
