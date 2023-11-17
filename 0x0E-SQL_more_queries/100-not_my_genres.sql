-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT DISTINCT tg.name FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id NOT IN
(SELECT tsg.genre_id FROM tv_show_genres tsg
       JOIN tv_shows ts ON ts.id = tsg.show_id
	WHERE ts.title = 'Dexter')
ORDER BY tg.name ASC;
