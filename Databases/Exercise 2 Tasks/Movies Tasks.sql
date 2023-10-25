USE movies

SELECT 
	movietitle,
	starname,
	address, 
	gender, 
	birthdate
FROM starsin 
JOIN moviestar ON starsin.starname = moviestar.name
WHERE movietitle = 'Terms of Endearment';


SELECT 
	starname 
FROM starsin
JOIN movie on starsin.movietitle = movie.title
WHERE studioname = 'MGM' 
AND movieyear = 1995;
