# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d ON e.departmentID = d.id
WHERE 
    3 >= (
        SELECT COUNT(DISTINCT e1.salary)
        FROM Employee e1
        WHERE e1.departmentID = e.departmentID
        AND e1.salary >= e.salary
        LIMIT 2
    )