# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales
INNER JOIN Product ON sales.product_id = product.product_id