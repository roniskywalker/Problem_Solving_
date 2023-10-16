Select  p.product_id, ifnull(round(sum(units * price)/sum(units),2),0) as average_price
from Prices p
left join UnitsSold u
on u.purchase_date >= p.start_date and u.purchase_date <= p.end_date and p.product_id = u.product_id
group by p.product_id;