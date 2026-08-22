class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #can use sorted method => But long!
        resolve = defaultdict(list)

        for s in strs :
            count = [0] * 26 #From a-z there are 26 character 
            for char in s :
                count[ord(char) - ord('a')] += 1
            resolve[tuple(count)].append(s)
        return list(resolve.values())   