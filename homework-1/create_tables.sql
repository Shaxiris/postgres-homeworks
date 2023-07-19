-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) UNIQUE NOT NULL,
	company_name text,
	contact_name varchar(50)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(50)
);

SELECT * FROM orders;
SELECT * FROM customers;
SELECT * FROM employees;