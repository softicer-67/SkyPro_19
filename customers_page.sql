-- Посчитать количество заказчиков
SELECT count(contact_name) FROM customers

-- Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики
SELECT distinct country, city FROM customers

-- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники 
-- из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
SELECT c.company_name, e.last_name, e.first_name, shippers, e.city
FROM orders
JOIN customers as c ON c.customer_id = orders.customer_id
JOIN employees as e ON e.employee_id = orders.employee_id
JOIN shippers ON shippers.shipper_id = orders.ship_via
WHERE c.city = 'London' AND e.city = 'London' AND shippers.company_name = 'Speedy Express'

-- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
SELECT contact_name, orders.order_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.order_id IS NULL;
