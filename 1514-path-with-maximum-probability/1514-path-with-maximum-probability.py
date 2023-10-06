class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for index,edge in enumerate(edges):
            graph[edge[0]].append((edge[1],succProb[index]))
            graph[edge[1]].append((edge[0],succProb[index]))
            
        probabilities = [0] * n 
        
        probabilities[start_node] = 0
        
        queue = [(-1,start_node)]
        
        while queue:
            probability,vertex = heappop(queue)
            probability *= -1
            if vertex == end_node:
                return probability
            # if probability < probabilities[vertex]:
            #     continue
            for child,child_prob in graph[vertex]:
                new_prob = probability * child_prob
                if new_prob > probabilities[child]:
                    heappush(queue,(-(new_prob),child))
                    probabilities[child] = new_prob
                
                
        return 0
                
            
            
        
            
