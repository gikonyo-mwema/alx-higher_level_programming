-- Script to list all cities of California

USE hbtn_0d_usa;

SET @california_id = (SELECT id FROM states WHERE name = 'California');

SELECT * FROM cities WHERE state_id = @california_id ORDER BY id ASC;
