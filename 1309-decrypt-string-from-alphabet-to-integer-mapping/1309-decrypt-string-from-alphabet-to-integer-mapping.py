class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {str(i):chr((ord('a') + i - 1)) for i in range(1,10)}
        d.update({f"{i}#":chr((ord('a') + i -1 )) for i in range(10,27)})
        
        output = ""
        right = len(s) - 1
        while right >= 0:
            if s[right] == "#":
                temp = ""
                for i in range(3):
                    temp = s[right] + temp
                    right -= 1
                print(temp)
                print(output)
                output = d[f'{temp}'] + output
            else:
                output = d[s[right]] + output
                right -= 1
        return output
                

                