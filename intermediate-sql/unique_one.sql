-- Return the unique countries from the films table
SELECT DISTINCT country 
FROM films;

-- Count the distinct countries from the films table
SELECT COUNT(DISTINCT country) AS count_distinct_countries
FROM films;


