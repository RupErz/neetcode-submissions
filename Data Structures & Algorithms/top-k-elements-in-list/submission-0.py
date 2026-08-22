class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashcount = {}
        # freq is a list that : index : number of freq, value : list of number
        # carry that frequency
        freq = [ []  for i in range(len(nums) + 1)]
        for i in nums :
            hashcount[i] = 1 + hashcount.get(i, 0)
        for i,v in hashcount.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k :
                    return res

            
