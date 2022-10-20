-- Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
select order_id, required_date, shipped_date from orders
order by required_date desc, shipped_date

-- Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
select avg(shipped_date - order_date), ship_country from orders
where ship_country = 'USA'
group by ship_country

-- Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)
select sum(unit_price * units_in_stock) from products
where discontinued <> 1
