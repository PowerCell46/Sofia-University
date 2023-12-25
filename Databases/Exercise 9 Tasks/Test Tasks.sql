CREATE DATABASE test;

use test;

CREATE TABLE Product(
    MAKER CHAR(1),
    MODEL CHAR(4) PRIMARY KEY,
    "TYPE" VARCHAR(7)
);

CREATE TABLE PRINTER(
    CODE INT PRIMARY KEY,
    MODEL CHAR(4) REFERENCES Product(MODEL),
    COLOR CHAR(1) DEFAULT 'n' CHECK(COLOR IN ('y', 'n')),
    PRICE DECIMAL(10, 2)
);

CREATE TABLE CLASSES(
	CLASS VARCHAR(50) PRIMARY KEY,
	"TYPE" CHAR(2) CHECK("TYPE" IN ('bb', 'bc'))
);

INSERT INTO PRODUCT
VALUES 
	('A', '1111', 'PC'),
	('B', '1112', 'Laptop'),
	('C', '1113', 'Printer');
	
INSERT INTO PRINTER
VALUES 
	(1, '1113', 'y', 120.20);

INSERT INTO PRODUCT	
VALUES 
	('A', '1114', 'Printer');

INSERT INTO PRINTER(CODE, MODEL)
VALUES 
	(2, '1114');

INSERT INTO CLASSES
VALUES 
	('ironclad', 'bb');


ALTER TABLE CLASSES
ADD BORE FLOAT;


ALTER TABLE PRINTER
DROP COLUMN PRICE;

DROP TABLE PRODUCT;
DROP TABLE PRINTER;
DROP TABLE CLASSES;

DROP DATABASE test;