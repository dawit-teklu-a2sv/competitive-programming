class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won_dict = {}
        lose_dict = {}
        for won,lose in matches:
            won_dict[won] = 1 + won_dict.get(won,0)
            lose_dict[lose] = 1 + lose_dict.get(lose,0)
        won_dict = {k:v for k,v in sorted(won_dict.items(),key = lambda x:x[0])}
        lose_dict = {k:v for k,v in sorted(lose_dict.items(),key = lambda x:x[0])}
        won_list = []
        lose_list = []
        for item in won_dict:
            if item not in lose_dict:
                won_list.append(item)
        for item in lose_dict:
            if lose_dict[item] == 1:
                lose_list.append(item)
        return [won_list,lose_list]

                

                