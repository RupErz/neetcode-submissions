class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        res, prev = 1, ""

        while R in range(len(arr)):
            if arr[R] > arr[R - 1] and prev != ">":
                res = max(res, R - L + 1)
                prev = ">"
                R += 1
            elif arr[R] < arr[R - 1] and prev != "<":
                res = max(res, R - L + 1)
                prev = "<"
                R += 1
            else:
            # This case is either violate the sign OR its eqal to prev value
            # Of course you can make multiple if make sure u reset prev state
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1 
                prev = ""
        return res
            