# Write your MySQL query statement below

select employee_id, case when count(department_id) = 1 then department_id else sum(case when primary_flag = 'Y' then 1 * department_id else 0 end) end as department_id
from Employee
group by employee_id
having department_id <> 0