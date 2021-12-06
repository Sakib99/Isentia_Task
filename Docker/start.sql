CREATE DATABASE carles_database;

CREATE USER 'python'@'localhost' IDENTIFIED BY 'sakib';
CREATE USER 'python'@'%' IDENTIFIED BY 'sakib';
GRANT ALL PRIVILEGES ON carles_database.* TO 'python'@'localhost';
GRANT ALL PRIVILEGES ON carles_database.* TO 'python'@'%';

USE carles_database;


CREATE TABLE web_sections_final (wesite_name VARCHAR(55),wesite_url VARCHAR(255),category VARCHAR(100),content VARCHAR(3000), time VARCHAR(50));
