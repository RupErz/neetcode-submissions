class Solution:
    def reorganizeString(self, s: str) -> str:
        # Create a freq list to fill up
        freq_list = {}
        for i in s:
            freq_list[i] = freq_list.get(i, 0) + 1

        max_freq = max(freq_list.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Create the max heap
        heap = [(-freq, char) for char, freq in freq_list.items()]
        heapq.heapify(heap)

        last_char = None
        last_freq = 0
        result = []
        while heap:
            # freq is negative, char is the character
            freq, char = heapq.heappop(heap)
            result.append(char)

            if last_freq < 0:
                heapq.heappush(heap, (last_freq, last_char))

            last_char = char
            last_freq = freq + 1 # Its negative ( max Heap )
        return "".join(result) 

        
