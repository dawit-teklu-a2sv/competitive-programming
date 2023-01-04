class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        temp = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp[i+j].append((j,mat[i][j]))
        d = {}
        for key,value in temp.items():
            d[key] = sorted(value,key=lambda x:x[0])
        print(d)
        output = []
        for key,value in d.items():
            if key % 2 == 1:
                for j in range(len(value)-1,-1,-1):
                    output.append(value[j][1])
            else:
                for j in range(len(value)):
                    output.append(value[j][1])
        return output
                
                
                