-- Script to list records with asame score
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
