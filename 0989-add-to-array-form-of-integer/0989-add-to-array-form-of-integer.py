class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        output = ""
        for item in num:
            output += str(item)
        output =  int(output) + k
        return [int(x) for x in str(output)]
        