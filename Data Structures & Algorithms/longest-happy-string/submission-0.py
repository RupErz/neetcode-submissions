class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # trie -> need string to build , we dont have it X
        # longest possible string -> not BFS (find shortest)
        # DFS or sliding window
        # DFS word[:3] [1:4] [2: 5] [3: 6] [len(w) - 3 : len(w)]
        # DFS is counting ALL paths -> way too inefficient
        # Greedy ? Build up the string greedily

        result = []

        # Turn into a max heap
        charList = [(a, "a"), (b, "b"), (c, "c")]
        freq = [(-amt, char) for amt, char in charList if amt > 0]
        heapq.heapify(freq)

        # Pop most freq for at most 2 times then alternate
        while freq:
            amount, nextChar = heapq.heappop(freq)

            # If last 2 is the same with next meaning we violate it
            if len(result) >= 2 and result[-2] == result[-1] == nextChar:
                # If we cannot find a 2nd largest to fill in - stop
                if not freq:
                    break 
                amt, ch = heapq.heappop(freq)
                result.append(ch)

                if amt + 1 != 0 :
                    heapq.heappush(freq, (amt + 1, ch))
                heapq.heappush(freq, (amount, nextChar))
            # Otherwise we are safely to extend
            else:
                result.append(nextChar)
                if amount + 1 != 0:
                    heapq.heappush(freq, (amount + 1, nextChar))

        return "".join(result)

            

            



