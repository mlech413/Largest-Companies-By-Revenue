DROP TABLE IF EXISTS companies;

CREATE TABLE companies ( rank INT, 
						name VARCHAR(100), 
						name_link VARCHAR(100), 
						symbol VARCHAR(10), 
						industry VARCHAR(100), 
						rev_usd_mil INT, 
						rev_growth_per VARCHAR(10), 
						employees INT, 
						headquarters_city VARCHAR(100), 
						headquarters_link VARCHAR(100), 
						headquarters_lat FLOAT, 
						headquarters_lon FLOAT );
						
SELECT * FROM companies;
SELECT COUNT(*) FROM companies;

DROP TABLE IF EXISTS stocks;

CREATE TABLE stocks ( symbol VARCHAR(10), 
					 date DATE, 
					 open DEC, 
					 high DEC, 
					 low DEC, 
					 close DEC, 
					 adj_close DEC, 
					 volume INT );
					 
SELECT * FROM stocks;
SELECT COUNT(*) FROM stocks;