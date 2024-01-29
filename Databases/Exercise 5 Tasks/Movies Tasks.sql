USE movies;

SELECT 
	name,
	(SELECT 
	COUNT(Distinct studioname)
FROM moviestar m2
JOIN STARSIN ON
	m2.NAME = STARSIN.STARNAME
JOIN MOVIE ON 
	starsin.MOVIETITLE = movie.TITLE
WHERE m2.NAME = moviestar.name) AS "Number of Studios"
FROM moviestar
JOIN STARSIN ON
	moviestar.NAME = STARSIN.STARNAME
JOIN MOVIE ON 
	starsin.MOVIETITLE = movie.TITLE
GROUP BY NAME;

SELECT 
	name,
	(SELECT 
	COUNT(Distinct studioname)
	FROM moviestar m2
	JOIN STARSIN ON
		m2.NAME = STARSIN.STARNAME
	JOIN MOVIE ON 
		starsin.MOVIETITLE = movie.TITLE
	WHERE m2.NAME = moviestar.name) as "Number of Studios"
FROM MOVIESTAR
left join STARSIN ON
	MOVIESTAR.name = STARSIN.STARNAME
left join movie on 
	STARSIN.MOVIETITLE = movie.TITLE;

SELECT STARNAME
FROM STARSIN
WHERE MOVIEYEAR > 1990
GROUP BY STARNAME
HAVING COUNT(*) >= 3;

-- Да се изведе средният брой филми, в които са се снимали актьорите

SELECT 
	AVG(avg_movies_per_current_actor)
FROM (SELECT 
--	MOVIESTAR.NAME,
	COUNT(MOVIETITLE) AS avg_movies_per_current_actor
FROM MOVIESTAR
LEFT JOIN STARSIN ON
	MOVIESTAR.NAME = STARSIN.STARNAME
GROUP BY MOVIESTAR.NAME) subquery;
