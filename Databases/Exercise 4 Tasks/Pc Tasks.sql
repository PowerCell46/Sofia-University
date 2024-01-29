use pc;

SELECT 
	product.model,
	pc.price
FROM PRODUCT
LEFT JOIN PC ON 
	PRODUCT.model = PC.model;

-- corrected version

SELECT 
	pc.model,
	price
FROM product
LEFT JOIN PC ON
	product.model = PC.model
WHERE type = 'PC'
ORDER BY product.model;


SELECT 
	MODEL,
	MAKER,
	TYPE
FROM PRODUCT 
WHERE 
model NOT IN (
	SELECT product.model FROM PRODUCT
	JOIN laptop on 
		product.model = laptop.model)
AND MODEL NOT IN (
	SELECT product.model FROM PRODUCT
	JOIN pc on 
		product.model = pc.model)
AND MODEL NOT IN (
	SELECT product.model FROM PRODUCT
	JOIN printer on 
		product.model = printer.model);
