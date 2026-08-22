class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures) 
        for i in range(len(temperatures) - 1):
            for j in range(i + 1,len(temperatures)):
                if temperatures[j] > temperatures[i] :
                    stack[i] = j - i
                    break
        return stack

