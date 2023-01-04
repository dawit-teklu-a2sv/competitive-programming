class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        temp = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp[i+j].append(mat[i][j])
        output = []   
        print(temp)
        for key,value in temp.items():
            if key % 2 == 0:
                for j in range(len(value)-1,-1,-1):
                    output.append(value[j])
            else:
                for j in range(len(value)):
                    output.append(value[j])
        return output