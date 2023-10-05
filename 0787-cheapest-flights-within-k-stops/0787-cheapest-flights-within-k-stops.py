class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        
#         graph = defaultdict(list)
        
#         for u,v,price in flights:
#             graph[u].append((v,price))

#         queue = [(0,-1,src)]
#         visited = set([(src,src)])
#         ans = float('inf')
#         while queue:
#             price,stop,v  = heappop(queue)
#             if stop <= k and v == dst:
#                 ans = min(ans,price)
            
#             for child in graph[v]:
#                 if (v,child) not in visited:
#                     visited.add((v,child))
#                     heappush(queue,(price + child[1],stop + 1,child[0]))
                
#         return ans if ans != float('inf') else -1

#         prices = [float('inf')] * n 
        
#         prices[src] = 0 
#         for i in range(k+1):
#             temp_prices = prices
            
#             for source,distination,price in flights:
#                 current_cheapest = temp_prices[distination]
#                 new_price = prices[source] + price
                
#                 if new_price < current_cheapest:
#                     temp_prices[distination] = new_price
            
#             prices = temp_prices 
            
#         return prices[dst] if prices[dst] != float('inf') else -1

        prices = [float('inf')] * n
        # set source price to 0 since it costs nothing to start at source
        prices[src] = 0
        
        for i in range(k + 1):
            # go through all edges
            temp_prices = list(prices)
            for source, dest, price in flights:
                current_cheapest = temp_prices[dest]
                new_price = prices[source] + price
                
                # update price if it is cheaper
                # new price is the cheapest price so far it costs to get to source + price to get to dest from source
                if new_price < current_cheapest:
                    temp_prices[dest] = new_price
            prices = temp_prices
        
        return prices[dst] if prices[dst] != float('inf') else -1
    


                    
            
            
        
        