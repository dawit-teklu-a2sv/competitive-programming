class Solution:
    def calculate(self, s: str) -> int:
        
        res=curr=prev = 0
        current_operation = "+"
        
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                    
                i -= 1
                if current_operation == "+":
                        res += curr
                        prev = curr
                elif current_operation == "-":
                        res -= curr
                        prev = -curr
                elif current_operation == "*":
                        res -= prev
                        prev = prev * curr
                        res += prev 
                elif current_operation == "/":
                        res -= prev
                        prev =   int(prev/curr)
                        res +=  prev
                curr = 0
            elif char != " ":
                current_operation = char
            i += 1
        return res