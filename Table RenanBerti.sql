-- Aula 31 Date 09/01/20
-- Create table in database MySql

-- Command Create Table
CREATE TABLE RenanBerti (
  ID int(11) NOT NULL /*AUTO_INCREMENT*/,
  Nome varchar(100) NOT NULL,
  Sobrenome varchar(100) NOT NULL,
  Idade int(11) NOT NULL,
  PRIMARY KEY (ID)
) /*ENGINE=InnoDB DEFAULT CHARSET=latin1*/

-- Commands Inserts
INSERT INTO topskills01.RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Renan','Berti',21);
INSERT INTO topskills01.RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Bruno','Berti',16);
INSERT INTO topskills01.RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Gabriel','Parasky',8);

-- Command Select row
SELECT ID, Nome, Sobrenome, Idade
FROM topskills01.RenanBerti;

--Command delete row
DELETE FROM topskills01.RenanBerti
WHERE ID=1;

--Command Update row
UPDATE topskills01.RenanBerti
SET Nome='Bruno', Sobrenome='Berti', Idade=16
WHERE ID=1;


