class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        temp_dict = defaultdict(int)
        for item1 in num1:
            for item2 in num2:
                if 'i' in item1 and 'i' in item2:
                    temp_dict['i2'] += int(item1[:-1]) * int(item2[:-1])
                elif 'i' in item1 or 'i' in item2:
                    if 'i' in item1:
                        temp_dict['i'] += int(item1[:-1]) * int(item2)
                    else:
                        temp_dict['i'] += int(item2[:-1]) * int(item1)
                
                else:
                    temp_dict['c'] += int(item1) * int(item2)
                    
        output = f"{temp_dict['c']-temp_dict['i2']}+{temp_dict['i']}i"
        return output