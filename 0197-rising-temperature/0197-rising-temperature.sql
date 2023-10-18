# Write your MySQL query statement below

select w2.id 
from weather w1 join weather w2 on datediff(w1.recorddate,w2.recorddate) = -1
where w2.temperature > w1.temperature