Tabelas SQL NO MySQL - 13-01-20
------------------------------------------------------
CREATE TABLE CLIENTE (
	CODIGO INT(11) NOT NULL,
	NOME VARCHAR(100) NOT NULL,
  SOBRENOME VARCHAR(100),
	IDADE INT(3) NOT NULL,
	GENERO VARCHAR(2) NOT NULL,
	EMAIL VARCHAR(25) NOT NULL,
	TELEFONE VARCHAR(50) NOT NULL,
	PRIMARY KEY (CODIGO)
)

CREATE TABLE ENDERECO (
	ID INT(11) NOT NULL AUTO_INCREMENT,
	LOGRADOURO VARCHAR(100) NOT NULL,
	NUMERO INT(11) NOT NULL,
	SIGLA varchar(5) NOT NULL,
	CIDADE VARCHAR(50) NOT NULL,
	BAIRRO VARCHAR(50) NOT NULL,
	CEP INT(11) NOT NULL,
	PRIMARY KEY (ID)
);

------------------------------------------------------
ALTER TABLE CLIENTE ADD COLUMN ENDERECO_ID INT(11) AFTER TELEFONE

ALTER TABLE CLIENTE ADD CONSTRAINT ENDERECO_FK FOREIGN KEY (ENDERECO_ID) REFERENCES ENDERECO (ID);
------------------------------------------------------










------------------------------------------------------

INSERT INTO RenanBerti (Nome,Sobrenome,Idade)
  VALUES ('Keunan','Passos',17), ('Lucas','Brito',18), ('Joao','Pessoa',40),
  		 ('Renan','Berti',21), ('Bruno','Berti',16), ('Gabriel','Parasky',8);

INSERT INTO Endereco (ID, LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP)
  VALUES (1, 'RUAAAAAA', '00', 'NAO SEI', 'VILA', 'BAU', '2536'), (2, 'RUA', '14', 'ALGO', 'VILAA', 'CASA', '362'),
  		 (3, 'RUA', '25', 'BAIRRO', 'CASA', 'CIDADE', '25896'), (4, 'RUAAA', '85', 'CARRO', 'VINTE', 'SETE', '475'),
         (5, 'AVENIDA', '85', 'OI', 'CASA', 'DEZ', '5214'), (6, 'RUAA', '85', 'TRINTA', 'QUARENTE', 'SETE', '965');

------------------------------------------------------
UPDATE CLIENTE SET ENDERECO_ID = 1 WHERE ID = 1;
UPDATE CLIENTE SET ENDERECO_ID = 2 WHERE ID = 2;
UPDATE CLIENTE SET ENDERECO_ID = 3 WHERE ID = 3;
UPDATE CLIENTE SET ENDERECO_ID = 4 WHERE ID = 4;
UPDATE CLIENTE SET ENDERECO_ID = 5 WHERE ID = 5;
UPDATE CLIENTE SET ENDERECO_ID = 6 WHERE ID = 6;

------------------------------------------------------
SELECT CONCAT(NOME, ' ', SOBRENOME) AS 'NOME COMPLETO' FROM cliente

SELECT * FROM CLIENTE AS C
JOIN ENDERECO AS E
ON C.ENDERECO_ID = E.ID

SELECT LPAD(NOME,2) FROM cliente;

SELECT C.ID, CONCAT(C.NOME,' ', C.SOBRENOME) AS 'NOME COMPLETO', E.*
FROM CLIENTE AS C
JOIN ENDERECO AS E
ON C.ENDERECO_ID = E.ID
WHERE C.NOME LIKE 'RE%'

----------------------------------------

set serveroutput on

CURSOR CURSOR1 IS  
    SELECT * FROM CLIENTE AS C
	 JOIN ENDERECO AS E
	 ON C.ENDERECO_ID = E.ID       
BEGIN
   FOR PESSOA IN CURSOR1 LOOP
   
    dbms_output.put_line('Nome do Cliente: ' || pessoa.nome || ' Cidade atual: ' || pessoa.cidade);
    
     
    IF pessoa.cidade = 'BLUMENAU' THEN 
        dbms_output.put_line(aluno.nome || ' faz parte da Uniasselvi Blumenau.');  
        UPDATE aluno set tipo = 'PRESENCIAL' where cidade = 'BLUMENAU' ;
            dbms_output.put_line('Tipo de Curso: PRESENCIAL ' );

    ELSE 
        dbms_output.put_line(aluno.nome || ' NAO faz parte da Uniasselvi de Blumenau.'); 
        UPDATE aluno set tipo = 'EAD' where cidade = 'JOINVILLE' ; 
            dbms_output.put_line('Tipo de Curso: EAD ');
         
    END IF;
       
    END LOOP;
END;



