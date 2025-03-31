CREATE DATABASE loginDB;

USE loginDB;

CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

INSERT INTO accounts (username, email, password) 
VALUES 
  ('AMRYB', 'amr10tuf@gmail.com', 'SecureP@ssw0rd123'),
  ('Youssef_GX', 'YOUSSEFGX2546@gmail.com', 'MyStr0ngP@ss!'),
  ('sama_fish4_3231', 'sama.elfishawy@gmail.com', 'Passw0rd!2025'),
  ('Yasminna', 'yasmin0039d@gmail.com', 'Reem$ecure2025');
