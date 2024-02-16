-- Script to list all record with score greater or equal to 10
SELECT name, score
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
