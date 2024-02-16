-- Script taht list all records excluding empty rows
SELECT name, score FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;
