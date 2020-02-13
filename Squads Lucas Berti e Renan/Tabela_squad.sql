----------#testando tabelas com foreigh key-----------------------------------

CREATE TABLE BACKEND (
        ID INT(11) NOT NULL AUTO_INCREMENT,
        LINGUAGEMBACKEND VARCHAR(200) NOT NULL,
        PRIMARY KEY (ID)
        );

CREATE TABLE FRONTEND (
        ID INT(11) NOT NULL AUTO_INCREMENT,
        LINGUAGEMFRONTEND VARCHAR(200) NOT NULL,
        PRIMARY KEY (ID)
        );

CREATE TABLE SGBDS (
        ID INT(11) NOT NULL AUTO_INCREMENT,
        NOME_DB VARCHAR(200) NOT NULL,
        PRIMARY KEY (ID)  
        );

CREATE TABLE SQUAD (
        ID INT(11) NOT NULL AUTO_INCREMENT,
        NAME_SQUAD VARCHAR(100) NOT NULL,
        DESCRICAO VARCHAR(200) NOT NULL,
        NUMERO_PESSOAS INT(5) NOT NULL,
        ID_BACKEND INT(11),
        ID_FRONTEND INT(11),
        ID_SGBDS INT(11),
        PRIMARY KEY (ID),
        FOREIGN KEY (ID_BACKEND) REFERENCES BACKEND (ID),
        FOREIGN KEY (ID_FRONTEND) REFERENCES FRONTEND (ID),
        FOREIGN KEY (ID_SGBDS) REFERENCES SGBDS (ID)
        );

-------------------------------------
INSERT INTO BACKEND 
        (
        LINGUAGEMBACKEND
        )
VALUES
        ('Python'),('Ruby'),('Pascal'),('Java'),('C#'),('C'),('Swift'),('PHP'),('JavaScript'),('Cobol')
     

INSERT INTO FRONTEND 
        (
        LINGUAGEMFRONTEND
        )
VALUES
        ('HTML'),('CSS'),('JavaScript')
        

INSERT INTO SGBDS 
        (
        NOME_DB
        )
VALUES
        ('MySQL'),('SQLite'),('Oracle'),('SQL Server')

