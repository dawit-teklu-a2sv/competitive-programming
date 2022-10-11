class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        output = [x for x in s]
        for i,a in enumerate(output):
            if a == '(':
                stack.append(i)
            elif a == ')':
                start = stack.pop() + 1
                end = i
                while start < end:
                    output[start],output[end] = output[end],output[start]
                    start += 1
                    end -= 1
        output = [item for item in output if item != '(' and item != ')']
        return "".join(output)
        