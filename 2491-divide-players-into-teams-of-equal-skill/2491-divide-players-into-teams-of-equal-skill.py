class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if len(skill) > 2:
            temp = skill[0] + skill[-1]
            l = 1
            r = len(skill) - 2
            while l <= r:
                if temp != skill[l] + skill[r]:
                    return -1
                l += 1
                r -= 1
        left = 0 
        right = len(skill)-1
        output = 0
        while left <= right:
            output += (skill[left] * skill[right])
            left += 1
            right -= 1
        return output
        
        