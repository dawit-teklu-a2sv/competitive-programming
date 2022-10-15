class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        max_ = 0
        
        for fruit in fruits:
            if (fruit == last_fruit or fruit == second_last_fruit):
                current_max += 1
            else:
                current_max  = last_fruit_count + 1
            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count  = 1
            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit
               
            max_ = max(max_,current_max)
        return max_
                
                

                