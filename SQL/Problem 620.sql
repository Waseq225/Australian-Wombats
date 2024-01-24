# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM (
    SELECT * 
    FROM Cinema 
    WHERE MOD(id, 2) <> 0
) AS movie
WHERE NOT description ='boring'
ORDER BY rating desc