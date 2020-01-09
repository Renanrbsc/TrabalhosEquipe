--procedure row span
CREATE PROCEDURE Add_loop_in_RenanBerti()
BEGIN
    DECLARE i int DEFAULT 1;
    WHILE i <= 50 DO
   		insert into RenanBerti (nome,sobrenome,idade) values ('Renan','Berti',21 ); 
        SET i = i + 1;
    END WHILE;
END

call Add_loop_in_RenanBerti()
--

--procedure row span
CREATE PROCEDURE IRINEU()
BEGIN
    DECLARE i int DEFAULT 1;
    WHILE i <= 50 DO
   		insert into Keunan (nome,sobrenome,idade) values ('IRINEU','Nao fui eu',2 ); 
        SET i = i + 1;
    END WHILE;
END

call IRINEU();
--

--Procedure delete span   
CREATE PROCEDURE IRINEUDELET()
BEGIN
   		Delete from keunan where nome = 'IRINEU'; 
END

CALL IRINEUDELET();
--
