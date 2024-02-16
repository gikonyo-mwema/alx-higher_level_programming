-- Average temp 
SELECT city, AVG(temperature_fahrenheit) AS average_temperature
FROM weather_data
GROUP BY city
ORDER BY average_temperature DESC;
