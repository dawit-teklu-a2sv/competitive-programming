class Solution:
    def interpret(self, command: str) -> str:
        d = {'G':'G','()':'o','(al)':'al'}
        
        left = 0
        output = ''
        while left < len(command):
            if command[left] == 'G':
                output += 'G'
                left += 1
            else:
                temp = ""
                while command[left] != ')':
                    temp += command[left]
                    left += 1
                output+= d[f'{temp})']
                left += 1
        return output