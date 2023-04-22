class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjL = [[] for _ in range(n)]
        
        for src,dst in edges:
            adjL[src].append(dst)
            adjL[dst].append(src)
            
        count = [0] * n 
        
        def dfs(index,parent):
            labelCount = defaultdict(int)
            
            for nbr in adjL[index]:
                if nbr == parent:
                    continue
                childLabelCount  = dfs(nbr,index)
                for key,value in childLabelCount.items():
                    labelCount[key] += value
            labelCount[labels[index]] += 1
            count[index] = labelCount[labels[index]]
            return labelCount
        dfs(0,0)
        return count
                    