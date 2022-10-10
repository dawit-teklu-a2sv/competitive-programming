class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = 0
        output = 0
        # sorted_arr = sorted(Counter(arr).items(),key= lambda item: -item[1])
        sorted_arr = {}
        for item in arr:
            if item in sorted_arr:
                sorted_arr[item] += 1
            else:
                sorted_arr[item] = 1
        sorted_arr = sorted(sorted_arr.items(),key=lambda item: -item[1])
        for k,v in sorted_arr:
            counter += v # how many items are popped
            output += 1
            if counter >= (len(arr)//2):
                break
        return output
                

            
        