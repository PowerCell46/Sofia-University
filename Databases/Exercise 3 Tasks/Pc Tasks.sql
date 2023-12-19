USE PC;

SELECT MAKER FROM PC
JOIN PRODUCT ON 
	PC.model = product.model
WHERE SPEED >= 500
GROUP BY MAKER;

SELECT * FROM laptop
WHERE SPEED < (
	SELECT TOP 1
	speed FROM PC
	ORDER BY speed ASC);


CREATE TABLE mostExpensiveMachines (
    model INT,
    price INT
);

INSERT INTO mostExpensiveMachines (model, price)
SELECT TOP 1 model, price
FROM laptop
ORDER BY price DESC;

INSERT INTO mostExpensiveMachines (model, price)
SELECT TOP 1 model, price FROM pc 
ORDER BY PRICE desc;

INSERT INTO mostExpensiveMachines (model, price)
SELECT TOP 1 model, price FROM PRINTER 
ORDER BY PRICE desc;

SELECT TOP 1 
	model 
FROM mostExpensiveMachines
ORDER BY price DESC;


SELECT TOP 1
	maker
FROM printer
JOIN product ON printer.model = product.model
WHERE color = 'y'
ORDER BY PRICE ASC;


SELECT TOP 1
	maker
FROM PC
JOIN PRODUCT on pc.model = product.model
ORDER BY 
	RAM ASC,
	SPEED DESC;
