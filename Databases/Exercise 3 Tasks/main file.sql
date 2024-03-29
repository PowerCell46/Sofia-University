USE movies

SELECT 
	movie.TITLE, 
	movie.YEAR,
	studio.name,
	studio.address
FROM movie
JOIN studio ON
movie.studioname = studio.name
WHERE movie.length> 120;


SELECT 
	studio.NAME,
	MOVIESTAR.name
FROM STUDIO
	JOIN MOVIE ON STUDIO.NAME = movie.STUDIONAME
	JOIN STARSIN ON MOVIE.TITLE = STARSIN.MOVIETITLE
	JOIN MOVIESTAR ON STARSIN.STARNAME = MOVIESTAR.NAME
ORDER BY studio.name;


SELECT 
	MOVIEEXEC.NAME
FROM MOVIESTAR
	JOIN STARSIN ON MOVIESTAR.NAME = STARSIN.STARNAME
	JOIN MOVIE ON STARSIN.MOVIETITLE = MOVIE.TITLE
	JOIN MOVIEEXEC ON MOVIE.PRODUCERC#= MOVIEEXEC.CERT#
GROUP BY MOVIEEXEC.NAME;


