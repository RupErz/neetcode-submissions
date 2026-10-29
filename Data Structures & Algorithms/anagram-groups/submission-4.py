class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for st in strs:
            group = [0] * 26
            for l in st:
                group[ord(l) - ord('a')] += 1
            if tuple(group) in anagram:
                anagram[tuple(group)].append(st)
            else:
                anagram[tuple(group)] = [st]
        
        result = []
        for k, v in anagram.items():
            result.append(v)
        return result       