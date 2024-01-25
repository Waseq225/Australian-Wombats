-- Write your MySQL query statement below
SELECT w1.id AS Id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = -1
AND w1.temperature > w2.temperature