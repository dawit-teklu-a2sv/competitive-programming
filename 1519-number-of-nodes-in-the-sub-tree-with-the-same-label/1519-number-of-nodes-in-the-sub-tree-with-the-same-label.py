class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjL = [[]for _ in range(n)]
        labels = [label for label in labels]
        count = [0] * n
        for src,dst in edges:
            adjL[src].append(dst)
            adjL[dst].append(src)

        
        def dfs(index,adjL,labels,count,parent):
            labelCount = defaultdict(int)
            for nbr in adjL[index]:
                if parent == nbr:
                    continue
                childLabelCount = dfs(nbr,adjL,labels,count,index)
                for label in childLabelCount.keys():
                    labelCount[label] += childLabelCount[label]
            labelCount[labels[index]] += 1
            count[index] = labelCount[labels[index]]
            return labelCount
        dfs(0,adjL,labels,count,0)
        return count