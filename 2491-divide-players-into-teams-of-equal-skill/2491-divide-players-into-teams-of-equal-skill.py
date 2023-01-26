class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0 
        right = len(skill)-1
        output = 0
        temp = skill[left] + skill[right] 
        while left <= right:
            if temp != skill[left] + skill[right]:
                return -1
            output += (skill[left] * skill[right])
            left += 1
            right -= 1
        return output
        
        