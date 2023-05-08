class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        n = len(recipes)
        for index in range(n):
            for item in ingredients[index]:
                graph[item].append(recipes[index])
                incoming[recipes[index]] += 1
                
        output = []
        queue = deque(supplies)
        while queue:
            f = queue.popleft()
            for item in graph[f]:
                incoming[item] -= 1
                if incoming[item] == 0:
                    output.append(item)
                    queue.append(item)
        return output


        
        
