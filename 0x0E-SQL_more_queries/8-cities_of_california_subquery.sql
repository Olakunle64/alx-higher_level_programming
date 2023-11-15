-- Write a script that lists all the cities of California that
-- can be found in the database hbtn_0d_usa.
-- The states table contains only one record where
-- name = California (but the id can be different, as per example).
-- Results must be sorted in ascending order by cities.id

SELECT c.id, c.name FROM cities c WHERE c.state_id =
	(SELECT id FROM states WHERE name = 'California') ORDER BY c.id ASC;
