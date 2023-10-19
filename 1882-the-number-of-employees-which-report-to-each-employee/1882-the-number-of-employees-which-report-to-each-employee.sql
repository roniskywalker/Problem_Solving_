# Write your MySQL query statement below

select e1.reports_to as employee_id, e2.name, e1.count as reports_count, e1.age as average_age
from (select reports_to, count(employee_id) as count, round(avg(age), 0) as age from Employees group by reports_to having reports_to is not null) e1
join Employees e2
on e1.reports_to = e2.employee_id
order by employee_id