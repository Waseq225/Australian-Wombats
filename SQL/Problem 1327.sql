# Write your MySQL query statement below
SELECT product_name, unit
FROM 
(SELECT product_id, SUM(unit) as unit
FROM Orders
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY product_id) AS O
JOIN Products P ON P.product_id = O.product_id
WHERE unit >= 100
