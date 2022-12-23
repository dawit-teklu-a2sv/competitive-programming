class Solution:
    # def countPairs(self, deliciousness: List[int]) -> int:
    #     dicts = {}
    #     count = 0
    #     for i in deliciousness:
    #         for j in range(22):
    #             if (2**j - i) in dicts:
    #                 count += dicts[(2**j) - i ]
    #         dicts[i] = 1 + dicts.get(i,0)
    #     return count % ((10**7) + 9)    
    def countPairs(self, deliciousness: List[int]) -> int:
        dicts={}
        count=0
        for i in deliciousness:
            if len(dicts)==0:
                dicts[i]=0
            for j in range(22):
                if (2**j)-i in dicts:
                    count+=dicts[(2**j)-i]  
            if i not in dicts:
                dicts[i]=1
            elif i in dicts or dicts[i]==0:
                dicts[i]+=1  
        return count % ((10**9)+7) 