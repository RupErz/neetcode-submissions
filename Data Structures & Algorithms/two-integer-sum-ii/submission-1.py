class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Req: Space : O(1) 
        # 1-indexed array : 1 , 2, 3, 4, 5, 6
        #array that index starting with 1
        left = 0
        right = 1
        while left < len(numbers) - 1:
            #Skipping values if both index r equal
            while numbers[left] == numbers[right]:
                left += 1
                right += 1
            #Check for the target
            while right < len(numbers):
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]
                else:
                    right += 1
            #Append all ptrs 
            left += 1
            right = left + 1
        