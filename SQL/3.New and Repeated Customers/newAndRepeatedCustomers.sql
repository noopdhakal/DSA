create table customer_orders (
order_id integer,
customer_id integer,
order_date date,
order_amount integer
);

INSERT INTO customer_orders VALUES
(1, 100, DATE '2022-01-01', 2000),
(2, 200, DATE '2022-01-01', 2500),
(3, 300, DATE '2022-01-01', 2100),
(4, 100, DATE '2022-01-02', 2000),
(5, 400, DATE '2022-01-02', 2200),
(6, 500, DATE '2022-01-02', 2700),
(7, 100, DATE '2022-01-03', 3000),
(8, 400, DATE '2022-01-03', 1000),
(9, 600, DATE '2022-01-03', 3000);

select * from customer_orders;

-- cte case statements aggregation


-- order_date, new_customer_count, repeat_customer_count

-- '01-JAN-22', 3, 0
-- '02-JAN-22', 2, 1
-- '02-JAN-22', 1, 2


with first_visit as (
select customer_id, min(order_date) as first_visit_date from customer_orders 
group by customer_id
), visit_flag as 
(select co.*, fv.first_visit_date, 
case when CO.ORDER_DATE = fv.first_visit_date then 1 else 0 end as first_visit_flag,
case when CO.ORDER_DATE != fv.first_visit_date then 1 else 0 end as repeat_visit_flag


from customer_orders CO
inner join first_visit fv on co.customer_id = fv.customer_id
order by order_id)

select order_date, sum(first_visit_flag) as no_of_new_customers, sum(repeat_visit_flag) as no_of_repeat_customer from visit_flag
group by order_date
;

select * from customer_orders;


