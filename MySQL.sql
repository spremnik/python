/*
Prednosti baze podataka:
- Konkuretnost
- Integritet
- Relacije
- Ponovna iskoristivost
- Sigurnost

Dvije razine neovisnosti:
-Fizička neovisnost
-Logička neovisnost

Modeli baza podataka:
-Relacijski
-Mrežni
-Hijerarhijski
-Objektni

Dizajniranje baze podataka:
-Analiza potreba
-Modeliranje podataka
-Implementacija
-Testiranje
-Održavanje

Entitet(Atributi) -> Tablica ili relacija.

Veza:
1-1 ili 1:1
1-N ili 1:Beskonacno
M-N ili Beskonacno:Beskonacno

ER dijagram:
-Entiteti - Pravokutnici
-Veze - Rombovi

Relacije među entitetima:
-Unarne
-Binarne
-N-arne

Edgar F. Codd - Rad - Dijeljene banke podataka.

Relacijski model:
-Relacija (Tablica,entitet);
-Atribut (Stupac);
-Domena atriburta (Dozvoljene vrijednosti stupca);
-Zapis atributa (Redak vrijednosti stupca);

Normalizacija - Proces organiziranja podataka radi minimalnog udvostručenja podataka.
-(1NF) Svaka vrijednost u stupcu mora biti jedinstvena i svi reci moraju imati jednak broj polja.
-(2NF) 1NF i retci moraju biti jednoznačno određeni i potpuno ovisni o primarnom ključu.
-(3NF) 2NF Svi stupci koji nisu primarni ključ ne smiju biti ovisni jedan o drugome.
-(BCNF) Boyce-Coddova NF  
-(4NF) ?
-(5NF) ?

SQL jezik:
-DCL - Jezik za "kontrolu" podataka
-DML - Jezik za "manipulaciju" podacima
-DDL - Jezik za "definiranje" podataka

DDL:
-CREATE - Stvara objekt npr. tablicu.
-DROP - Briše postojeći objekt.
-ALTER - Mijenja postojeći objekt.

DCL:
-GRANT - Korisnika ovlašćuje za rad s objektima baze.
-REVOKE - Briše ili smanjuje ovlasti korisnika na objektima baze.

DML:
(Glavni dio)
-INSERT - Upisuje retke u postojeću tablicu.
-UPDATE - Mijenja vrijednosti postojećeg retka.
-MERGE - Spaja podatke iz više tablica.
-DELETE - Briše postojeće retke iz tablice.
-TRUNCATE - Briše sve podatke iz tablice.

(Rad s transakcijama)
-BEGIN WORK ili START TRANSACTION ili BEGIN - Označava početak transakcije.
-SAVEPOINT naziv - Označava spremanje dijela transakcije do te točke.
-COMMIT ili COMMIT WORK - Označava kraj transakcije.
-ROLLBACK TO SAVEPOINT naziv - Vraća stanje na SAVEPOINT naziv ili ako ga nema na COMMIT ili ROLLBACK
-ROLLBACK - Vraća stanje na zadnji COMMIT ili ROLLBACK.

(Upiti)
-SELECT - Dohvaća retke iz tablice.
	-FROM - Iz koje tablice.
	-WHERE - Koje retke treba dohvatiti.
	-GROUP BY - Slaže dobivene retke u grupe prema vrijednosti.
	-HAVING - Identifikacija redaka nakon GROUP BY koje treba dohvatiti.
	-ORDER BY - Sortira rezultirani skup prema stupcu.

Tipovi podataka:
(Cjelobrojni, točno prikazivi)
-tinyint => 0 do 255 ili -128 do 127
-smallint => od -32768 do 32767 ili od 0 do 65535
-bigint => od -9223372036854775808 do 9223372036854775807 ili od 0 do 18446744073709551615.
-bit => Najviše 64 bita. 
-decimal,numeric => Broj fiksne preciznosti, 64 znamenke, od toga najviše 30 decimala. Standardni broj znamenki je 10.

(Približno prikaziv vrijednosti)
-double - od 1,79 * 10 ^ 308 do 1,79 * 10 ^ 308
-float - od 3,40 * 10 ^ 38 do 3,40 * 10 ^ 38

(Datum i vrijeme)
-date - Nadnevak od 01.01.0001. do 31.12.9999. s preciznošću od 1 dana.
-datetime - Nadnevak i vrijeme od 01.01.0001. u 00:00:00 do 31.12.9999. 23:59:59 s preciznošću od 1 sekunde.
-time - Prikazuje vrijeme od -838:59:59 do 838:59:59 s preciznošću od 1 sekunde.

(Znakovi)
-char, nchar - Unicode znakovi, fiksna duljina. Najviše 255 znakova.
-varchar, nvarchar - Unikod znakovi, varijabilna duljina. Najviše 65535 znakova.
-tinytext - unikod znakovi, varijabilne duljine. Najviše 255 znakova.
-text - unikod znakovi, varijabilne duljine. Najviše 65535 znakova.
-mediumtext - unikod znakovi, varijabilne duljine. Najviše 16777215 znakova.
-longtext - unikod znakovi, varijabilne duljine. Najviše 4294967295 znakova.
-ntext - unikod znakovi, varijabilne duljine. Najviše 1073741823 znakova.

(Binarne vrijednosti) 
-tinyblob - Binarni podaci, varijabilne duljine. Najviše 255 byteova.
-blob - Binarni podaci, varijabilne duljine. Najviše 65535 byteova.
-mediumblob - Binarni podaci, varijabilne duljine. Najviše 16777215 byteova.
-longblob - Binarni podaci, varijabilne duljine. Najviše 4294967295 byteova.

(Ostali tipovi podataka)
-cursor
-enum
-set

Ograničenja:
-NOT NULL
-UNIQUE
-PRIMARY KEY
-FOREIGN KEY
-INDEX

Agregatne funkcije(Najčešće korištene):
-AVG
-COUNT
-MIN
-MAX
-SUM

*/
CREATE DATABASE upisi;
SHOW DATABASES;
CREATE TABLE polaznici(
	sifra				INT,
	ime 				CHAR(50),
	prezime				CHAR(50),
	mjesto_stanovanja	CHAR(25)
);
SHOW TABLES;
DESC polaznici;
USE upisi;
ALTER TABLE polaznici ADD broj_telefona INT;
DESC polaznici;
USE upisi;
ALTER TABLE polaznici CHANGE broj_telefona br_tel CHAR(20);
DESC polaznici;
USE upisi;
ALTER TABLE polaznici DROP COLUMN br_tel;
DESC polaznici;
USE upisi;
DROP TABLE polaznici;
USE mysql;
DROP DATABASE upisi;
CREATE DATABASE upisi;
USE upisi;
DROP TABLE IF EXISTS polaznici;
CREATE TABLE polaznici(
	sifra				INT 		NOT NULL,
	ime 				CHAR(50) 	NOT NULL,
	prezime				CHAR(50) 	NOT NULL,
	mjesto_stanovanja	CHAR(25)
);
DESC polaznici;
USE upisi;
ALTER TABLE polaznici ADD unique ime_pr_jd(ime,prezime);
DESC polaznici;
USE upisi;
DROP TABLE IF EXISTS polaznici;
CREATE TABLE polaznici(
	sifra				INT 		NOT NULL,
	ime 				CHAR(50) 	NOT NULL,
	prezime				CHAR(50) 	NOT NULL,
	mjesto_stanovanja	CHAR(25),
	PRIMARY KEY(sifra)
);
USE upisi;
CREATE TABLE tecajevi(
	sifra 				CHAR(3) 	NOT NULL,
	naziv_tecaja		CHAR(25)	NOT NULL,
	PRIMARY KEY(sifra)
);
USE upisi;
CREATE TABLE upisi(
sifra_polaznika 	INT,
sifra_tecaja 		CHAR(3),
PRIMARY KEY pk_sifre(sifra_polaznika,sifra_tecaja),
INDEX sif_pol(sifra_polaznika),
INDEX sif_tec(sifra_tecaja),
FOREIGN KEY(sifra_polaznika) REFERENCES polaznici(sifra),
FOREIGN KEY(sifra_tecaja) REFERENCES tecajevi(sifra)
);
DESC polaznici;
DESC tecajevi;
DESC upisi;
SHOW TABLE STATUS LIKE 'polaznici';
SHOW TABLE STATUS LIKE 'tecajevi';
SHOW TABLE STATUS LIKE 'upisi';
USE upisi;
INSERT INTO polaznici VALUES (1,'Josipa','Mikulić','Zagreb');
SELECT * FROM polaznici;
USE upisi;
INSERT INTO polaznici VALUES 
(2,'Ivana','Horvat','Varaždin'),
(3,'Stipe','Babić','Zadar'),
(4,'Ante','Bilić','Split'),
(5,'Petar','Jukić','Zagreb'),
(6,'Luka','Ban','Dubrovnik'),
(7,'Ana','Perković','Sinj'),
(8,'Roko','Marić','Šibenik'),
(9,'Borna','Radić','Rijeka'),
(10,'Frano','Ivić','Osijek');
USE upisi;
INSERT INTO tecajevi VALUES 
('P01','Osnove rada PC računala'),
('P02','Microsoft Word'),
('D01','SQL osnove'),
('O01','Računalni operator'),
('O02','Programski jezi C'),
('O03','Grafički dizajner');
USE upisi;
INSERT INTO upisi VALUES 
(1,'P01'),
(1,'P02'),
(2,'D01'),
(3,'O01'),
(4,'P02'),
(4,'O01'),
(5,'P01'),
(6,'D01'),
(6,'P02'),
(6,'O02'),
(7,'P01'),
(8,'O03'),
(9,'P02'),
(10,'P01'),
(10,'D01');
USE upisi;
SELECT 	sifra 				AS 	Oznaka,
		ime 				AS 	'Ime osobe',
		prezime				AS 	'Prezime osobe',
		mjesto_stanovanja 	AS 	'Mjesto stanovanja'
FROM polaznici;
USE upisi;
SELECT 	sifra 				AS 	Oznaka,
		ime 				AS 	'Ime osobe',
		prezime				AS 	'Prezime osobe',
		mjesto_stanovanja 	AS 	'Mjesto stanovanja',
		sifra*5				AS 	'Oznaka x 5'
FROM polaznici;
USE upisi;
SELECT * FROM polaznici ORDER BY ime;
USE upisi;
SELECT * FROM polaznici ORDER BY mjesto_stanovanja DESC;
USE upisi;
SELECT * FROM polaznici ORDER BY sifra ASC;
USE upisi;
SELECT DISTINCT mjesto_stanovanja FROM polaznici;
USE upisi;
SELECT	mjesto_stanovanja FROM polaznici GROUP BY mjesto_stanovanja;
USE upisi;
SELECT * FROM polaznici LIMIT 3;
USE upisi;
SELECT * FROM polaznici LIMIT 1,2;
USE upisi;
SELECT * FROM polaznici WHERE mjesto_stanovanja = 'Split';
USE upisi;
SELECT sifra,ime,sifra%2 AS 'Parna šifra' FROM polaznici;
USE upisi;
SELECT * FROM upisi WHERE sifra_tecaja='P01' OR sifra_tecaja='P02';
USE upisi;
SELECT * FROM polaznici WHERE sifra=1 OR sifra=3 OR sifra=5;
USE upisi;
SELECT ime,prezime FROM polaznici WHERE NOT mjesto_stanovanja='Varaždin';
USE upisi;
SELECT ime,prezime FROM polaznici WHERE mjesto_stanovanja='Split' AND sifra > 2 ;
USE upisi;
SELECT * FROM polaznici,tecajevi LIMIT 0,1000;
USE upisi;
UPDATE polaznici SET mjesto_stanovanja = 'Samobor' WHERE ime = 'Petar' and mjesto_stanovanja = 'Zagreb'; 
USE upisi;
DELETE FROM polaznici WHERE sifra=6;
USE upisi;
TRUNCATE TABLE upisi;

/*
----------------------------------------
Bucky 
----------------------------------------
*/

SELECT id,name,state FROM customers WHERE state IN ('ca','ny','nc');
SELECT id,name,state FROM customers WHERE state NOT IN ('ca','ny','nc');
SELECT name FROM items WHERE name LIKE 'new%';
SELECT name FROM items WHERE name LIKE 'new%';
SELECT city FROM customers WHERE city LIKE 'h%d';
SELECT name FROM items WHERE name LIKE '_ boxes%';
SELECT name FROM items WHERE name REGEXP 'new';
SELECT name FROM items WHERE name REGEXP '.boxes';
SELECT name FROM items WHERE name REGEXP 'gold|car';
SELECT name FROM items WHERE name REGEXP '[12345] boxes';
SELECT name FROM items WHERE name REGEXP '[^12345] boxes';
SELECT name FROM items WHERE name REGEXP '[^1-5] boxes';
SELECT name FROM items WHERE name REGEXP '[a-z] new';
SELECT CONCAT(city, ' - ', state) FROM customers;
SELECT CONCAT(city, ' - ', state) AS nova_adresa FROM customers;
SELECT name,cost,cost-1 AS prodajna_cijena FROM items;
SELECT name,UPPER(name) AS VelikaSlovaIME FROM customers;
SELECT cost,SQRT(cost) AS korijenCijene FROM items;
SELECT AVG(cost) AS prosjek FROM items;
SELECT SUM(bids) AS ponude FROM items;
SELECT COUNT(name) AS brojPonudaProdavaca FROM items WHERE seller_id=6;
SELECT AVG(cost) AS prosjecnaCijenaProdavaca FROM items WHERE seller_id=6;
SELECT COUNT(*) AS brojStvari, MAX(cost) as najvecaCijena, AVG(cost) AS prosjecnaCijena FROM items WHERE seller_id=12;
SELECT seller_id AS Oznaka, COUNT(*) AS brojStvari FROM items GROUP BY seller_id;
SELECT seller_id AS Oznaka, COUNT(*) AS brojStvari FROM items GROUP BY seller_id HAVING COUNT(*) >= 3;
SELECT seller_id AS Oznaka, COUNT(*) AS brojStvari FROM items GROUP BY seller_id HAVING COUNT(*) >= 3 ORDER BY brojStvari DESC;
SELECT name AS ime, cost AS cijena FROM items WHERE cost>(SELECT AVG(cost) FROM items) ORDER BY cost DESC;
SELECT name, MIN(cost) FROM items WHERE name LIKE '%boxes%' AND seller_id IN(SELECT seller_id FROM items WHERE name LIKE '%boxes%');
SELECT customers.id,customers.name,items.name,items.cost FROM customers,items WHERE customers.id = seller_id ORDER BY customers.id;
SELECT c.id,c.name,i.name,i.cost FROM customers AS c,items AS i WHERE c.id = seller_id ORDER BY c.id;
SELECT customers.name,items.name FROM customers LEFT OUTER JOIN items ON customers.id = seller_id;
SELECT name,cost,bids FROM items WHERE bids>190 UNION SELECT name,cost,bids FROM items WHERE cost>1000;
SELECT name,cost,bids FROM items WHERE bids>190 UNION ALL SELECT name,cost,bids FROM items WHERE cost>1000;
ALTER TABLE items ADD FULLTEXT(name); SELECT name,cost FROM items WHERE Match(name) Against('baby');
SELECT name,cost FROM items WHERE Match(name) Against('+baby' IN BOOLEAN MODE);
SELECT name,cost FROM items WHERE Match(name) Against('+baby -coat' IN BOOLEAN MODE);
CREATE TABLE bacon(
id INT NOT NULL AUTO_INCREMENT,
username VARCHAR(30) NOT NULL,
password VARCHAR(20) NOT NULL,
PRIMARY KEY (id)
);