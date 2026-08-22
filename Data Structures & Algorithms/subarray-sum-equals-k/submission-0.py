class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0

        # We currently at sum = 0 so count as 1
        sum_dict = {0: 1}

        for n in nums:
            prefix_sum += n

            # If we found it means:
            # Somewhere in the array up to this point has
            # total sum of prefix - k
            if prefix_sum - k in sum_dict:
                result += sum_dict[prefix_sum - k]
            sum_dict[prefix_sum] = sum_dict.get(prefix_sum, 0) + 1
        return result
        
        # PrefixSum - k = N
        # with N: if we have x prefix sum total of N, that means
        # if we get rid of x these prefix our array can reach k
        # e.g: 4 - 3 = 1, but we have 1 : 2, that means there are 2 prefixsum
        # reach 1, if we chop off these prefixsum of 1 we got k
        # So thats why our result + 2 

        # 1st: Brute Force ( use recursion )
        # go to next number : == k
        # stop end of array 

        