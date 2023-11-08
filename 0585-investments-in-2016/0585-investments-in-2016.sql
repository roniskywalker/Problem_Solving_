# Write your MySQL query statement below

with cte as
(select distinct i1.*
from Insurance i1
left join Insurance i2
on i1.tiv_2015 = i2.tiv_2015
where i1.pid <> i2.pid and concat(i1.lat,',', i1.lon) not in (select concat(lat,',',lon)
from Insurance
group by lat, lon
having count(pid) > 1))

select round(sum(tiv_2016), 2) as tiv_2016
from cte