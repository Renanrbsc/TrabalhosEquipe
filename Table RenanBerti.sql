-- Aula 31 Date 09/01/20
-- Create table in database MySql

-- Command Create Table Pessoa
CREATE TABLE RenanBerti (
  ID int(11) NOT NULL AUTO_INCREMENT,
  Nome varchar(100) NOT NULL,
  Sobrenome varchar(100) NOT NULL,
  Idade int(11) NOT NULL,
  ENDERECO_ID INT NULL;
  CONSTRAINT RenanBerti_PK PRIMARY KEY (ID)
  CONSTRAINT RenanBerti_FK FOREIGN KEY (ENDERECO_ID) REFERENCES RenanBerti_Endereco(ID unique);
)
-----------------------------------------------------------

-- Command Create Table Endereco
CREATE TABLE RenanBerti_Endereco (
	ID unique INT auto_increment NOT NULL,
	LOGRADOURO varchar(50) NOT NULL,
	NUMERO NUMBER(5) NOT NULL,
	COMPLEMENTO varchar(100) NULL,
	BAIRRO varchar(25) NOT NULL,
	CIDADE varchar(25) NOT NULL
	CEP varchar(100) NOT NULL,
	CONSTRAINT RenanBerti_Endereco_PK PRIMARY KEY (ID unique)
)
-----------------------------------------------------------

-- Commands Inserts
INSERT INTO RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Renan','Berti',21);
INSERT INTO RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Bruno','Berti',16);
INSERT INTO RenanBerti (Nome,Sobrenome,Idade)
	VALUES ('Gabriel','Parasky',8);

INSERT INTO RenanBerti (Nome,Sobrenome,Idade)
  VALUES ('Keunan','Passos',17), ('Lucas','Brito',18), ('Joao','Pessoa',40);

-- Command Select row
SELECT ID, Nome, Sobrenome, Idade
FROM RenanBerti;

SELECT concat(Nome,' ',Sobrenome) as 'Nome Completo', Idade
FROM RenanBerti;

--Command delete row
DELETE FROM RenanBerti
WHERE ID=1;

--Command Update row
UPDATE RenanBerti
SET Nome='Bruno', Sobrenome='Berti', Idade=16
WHERE ID=1;


