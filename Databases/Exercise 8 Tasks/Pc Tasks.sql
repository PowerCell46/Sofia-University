USE PC;

INSERT INTO PRODUCT(maker, model, type)
VALUES 
	('C', '1100', 'PC');

INSERT INTO PC(code, model, speed, ram, hd, cd, price)
VALUES 
	(12, '1100', 2400, 2048, 500, '52x', 299);

DELETE FROM PC
WHERE MODEL = '1100';

DELETE FROM PRODUCT 
WHERE MODEL = '1100';

INSERT INTO LAPTOP(code, model, speed, ram, hd, price, screen)
SELECT 
	code + 100,
	model,
	speed, 
	ram, 
	hd,
	price + 500,
	15
FROM PC;

DELETE FROM LAPTOP 
WHERE model IN (
	SELECT laptop.model FROM laptop
	JOIN PRODUCT ON 
		LAPTOP.model = product.model
	WHERE maker NOT IN (
	SELECT maker FROM product
	JOIN PRINTER ON 
		product.model = printer.model
	GROUP BY maker
	)
);

SELECT * FROM PRODUCT;

UPDATE PRODUCT
SET maker = 'A'
WHERE maker = 'B';

UPDATE PC
SET 
	price = price / 2,
	hd = hd + 20;

UPDATE laptop
SET screen = screen + 1
WHERE model IN 
(
	SELECT laptop.model FROM laptop
	JOIN product ON
		laptop.model = product.model
	WHERE maker = 'B'
);
