REPLACE('','','')
--# Funcao REPLACE procura caracteres e os modifica por outro caracter
--- REPLACE('VARIAVEL OU STRING','CARACTER CONTIDO','CARACTER PARA MODIFICAR')
--- REPLACE('ACsou uma variavel','AC','nao ')
--- RETURN 'nao sou uma variavel'
UPDATE ENDERECO SET LOGRADOURO = REPLACE(LOGRADOURO,SIGLA,'') WHERE ID = 200
SELECT REPLACE(LOGRADOURO,SIGLA,'') WHERE ID = 200
------------------------------------------------------------------------------
