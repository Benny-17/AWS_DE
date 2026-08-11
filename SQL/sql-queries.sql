
--- to see table names 
SELECT table_name
FROM user_tables;

---checking which database/instance you're connected to:
SELECT * FROM GLOBAL_NAME;
--or--
SELECT SYS_CONTEXT('USERENV','DB_NAME') FROM DUAL;

-- to see  current schema/user, e.g. 'HR'
SELECT USER FROM DUAL;              -- current schema/user, e.g. 'HR'

SELECT OBJECT_NAME, OBJECT_TYPE
FROM USER_OBJECTS;     

---
SELECT OBJECT_TYPE, COUNT(*)
FROM USER_OBJECTS
GROUP BY OBJECT_TYPE;


