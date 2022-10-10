class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = 0
        output = 0
        sorted_arr = sorted(Counter(arr).items(),key= lambda item: -item[1])
        for k,v in sorted_arr:
            counter += v # how many items are popped
            output += 1
            if counter >= (len(arr)//2):
                break
        return output
                

            
        