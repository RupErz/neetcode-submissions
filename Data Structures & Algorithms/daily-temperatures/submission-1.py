class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [0] * len(temperatures) 
        # for i in range(len(temperatures) - 1):
        #     for j in range(i + 1,len(temperatures)):
        #         if temperatures[j] > temperatures[i] :
        #             stack[i] = j - i
        #             break
        # return stack
        # This solution not optimal

        res = [0] * len(temperatures) 
        stack = []  # This is a stack with each value is [temp, index]
        # [ [a,b], [c,d], ...]
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop() #[temp, idx]
                res[stackIdx] = idx - stackIdx
            stack.append([temp, idx])
        return res


