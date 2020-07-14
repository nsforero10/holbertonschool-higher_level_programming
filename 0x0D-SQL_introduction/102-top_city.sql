-- Shows top 3 average temperature
-- Shows top 3 average temperature
SELECT city, AVG(values) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3; 
