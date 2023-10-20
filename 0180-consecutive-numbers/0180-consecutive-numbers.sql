# Write your MySQL query statement below

with cte as
(select id, lead(num, 1) over() as next_1, lead(num, 2) over() as next_2 from Logs)

select distinct l.num as ConsecutiveNums
from Logs l
join cte
on l.id = cte.id
where num = next_1 and num = next_2