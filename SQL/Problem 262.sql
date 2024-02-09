# Write your MySQL query statement below

SELECT 
    request_at as Day, 
    ROUND(Sum(cancelled_trips)/Count(id),2) AS 'Cancellation Rate'
FROM
    (SELECT id          
        , request_at
        , CASE WHEN status != 'completed'  THEN 1 ELSE 0 END AS cancelled_trips
FROM Trips T
    WHERE client_id IN (SELECT users_id FROM Users WHERE banned ='No')
    AND driver_id IN (SELECT users_id FROM Users WHERE banned ='No')
    AND request_at BETWEEN DATE("2013-10-01") AND DATE("2013-10-03")
) as t
GROUP BY request_at 
