class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n #inf means unreachable
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices.copy()

            for s, d, c in flights: 
                # If start is unreachable then skips
                if prices[s] != float("inf"):
                    tmp[d] =  min(tmp[d], prices[s] + c)
            prices = tmp
        
        return prices[dst] if prices[dst] != float("inf") else -1



            
