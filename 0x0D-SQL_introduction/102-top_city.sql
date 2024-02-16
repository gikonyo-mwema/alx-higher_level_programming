-- Script to average temperature in descendign order
SELECT city, AVG(temperature) AS average_temperature
FROM weather_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
