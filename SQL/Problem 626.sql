# Write your MySQL query statement below

SELECT 
S1.id,
CASE WHEN S1.id%2 = 0 
     THEN (SELECT student FROM Seat S2 WHERE S1.id-1 = S2.id ) 
     ELSE 
        CASE 
            WHEN (SELECT student FROM Seat S2 WHERE S1.id+1 = S2.id ) IS NOT NULL
            THEN (SELECT student FROM Seat S2 WHERE S1.id+1 = S2.id )
            ELSE S1.student
        END
END as student
FROM Seat S1
ORDER BY S1.id