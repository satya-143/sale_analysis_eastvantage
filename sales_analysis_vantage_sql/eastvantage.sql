WITH customer_sales_temp_cte AS (
select s.sales_id,s.customer_id,c.age
from (select customer_id,sales_id 
	  from sales) s
     left join
     (select customer_id , age  
      from customers) c
     on s.customer_id=c.customer_id
) 
,
orders_items_temp_cte AS (
select o.sales_id,o.quantity,i.item_name
from (select item_id,IFNULL(quantity,0) as quantity,sales_id
      from orders) o
     left join
     (select item_id,item_name
     from items) i
     on o.item_id=i.item_id
)
,
cust_sales_orders_item_cte AS (
select cstc.customer_id,cstc.age,oitc.sales_id,oitc.item_name,oitc.quantity   
from orders_items_temp_cte oitc
left join
(select * FROM customer_sales_temp_cte) cstc
on oitc.sales_id = cstc.sales_id
)

select * from
(select customer_id,age,item_name,sum(quantity) as quantity
from cust_sales_orders_item_cte csoic
GROUP BY customer_id,age,item_name) result_set
where result_set.quantity != 0
      and result_set.age >= 18 and result_set.age <= 35
    
      