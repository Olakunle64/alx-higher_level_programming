-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT DISTINCT ts.title FROM tv_shows ts
JOIN tv_show_genres tsg
ON ts.id NOT IN
(SELECT tsg.show_id FROM tv_show_genres tsg
	JOIN tv_genres tg
	ON tsg.genre_id = tg.id
	WHERE tg.name = 'Comedy')
ORDER BY ts.title ASC;
