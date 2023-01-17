class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # swaps = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)-i-1):
        #         if heights[j] <  heights[j+1]:
        #             heights[j],heights[j+1] = heights[j+1],heights[j]
        #             names[j],names[j+1] = names[j+1],names[j]
        #             swaps += 1
        #     if swaps == 0:
        #         break
        for i in range(len(heights)):
            current_max_index = i
            for j in range(i,len(heights)):
                if heights[j]  > heights[current_max_index]:
                    current_max_index = j
            heights[i],heights[current_max_index] = heights[current_max_index],heights[i]
            names[i],names[current_max_index] = names[current_max_index],names[i]
        return names
        
            