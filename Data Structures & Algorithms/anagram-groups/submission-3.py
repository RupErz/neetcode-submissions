class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each strings and use hashmap to group them
        # [eat, tea, tan, ate, nat, bat]
        # eat -> sort: tea -> res[tea] = [eat]
        # tea -> sort: tea -> res[tea] = [eat, tea]
        # * Use the sorted one as key     


        # only lowercase english letters, 26 chars 
        # just use array bro.
        hashmap = defaultdict(list)

        for w in strs:
            key = [0] * 26
            for c in w: 
                offset = ord(c) - ord('a')
                key[offset] += 1
            hashmap[tuple(key)].append(w)
        
        return list(hashmap.values())
            
            



