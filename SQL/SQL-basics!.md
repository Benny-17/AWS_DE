#  Oracle SQL Recap & Handbook

---

## 1. Database (DB)

> **TL;DR:** A database is one big organized bucket that holds all related data, grouped into schemas.

```
Database
   ↓
Schemas
```

**Example** — checking which database/instance you're connected to:
```sql
SELECT * FROM GLOBAL_NAME;
-- or
SELECT SYS_CONTEXT('USERENV','DB_NAME') FROM DUAL;
```

---

## 2. Schema

> **TL;DR:** A schema = one user's personal workspace inside the database, holding all the tables/views/etc. they own.

```
Database
   ↓
HR Schema
   ↓
Objects
```

**Example** — see which schema (user) you're currently in, and list its objects:
```sql
SELECT USER FROM DUAL;              -- current schema/user, e.g. 'HR'

SELECT OBJECT_NAME, OBJECT_TYPE
FROM USER_OBJECTS;                  -- all objects owned by current schema
```

---

## 3. Database Objects

> **TL;DR:** Objects are the actual "things" stored inside a schema — tables hold data, and everything else (views, indexes, sequences, etc.) supports or reshapes that data.

**Important**
-  Table
-  View
-  Index
-  Materialized View (MVIEW)
-  Global Temporary Table (GTT)

**Other Objects**
- Sequence, Procedure, Function, Trigger, Package, Synonym, Database Link

**Example** — list object types that exist in your schema:
```sql
SELECT OBJECT_TYPE, COUNT(*)
FROM USER_OBJECTS
GROUP BY OBJECT_TYPE;
```

---

## 4. Table

> **TL;DR:** A table is rows × columns — the actual data storage unit. Row = record, Column = field/attribute.

```
EMPLOYEES

EMP_ID | FIRST_NAME | SALARY
-----------------------------
101    | John       | 50000
102    | Alice      | 60000
```

**Example** — creating and viewing a table's structure:
```sql
CREATE TABLE EMPLOYEES (
    EMP_ID     NUMBER,
    FIRST_NAME VARCHAR2(50),
    SALARY     NUMBER(10,2)
);

DESC EMPLOYEES;   -- shows column name, null?, datatype
```

---

## 5. Data Types

> **TL;DR:** Every column must declare what kind of value it stores — number, text, or date/time.

| Data Type | Stores                           |
|-----------|-----------------------------------|
| NUMBER    | Numbers                          |
| VARCHAR2  | Variable-length text              |
| CHAR      | Fixed-length text                 |
| DATE      | Date & Time                       |
| TIMESTAMP | Date & Time + Fractional Seconds  |

**Example**
```sql
CREATE TABLE SAMPLE_TYPES (
    ID          NUMBER,
    CODE        CHAR(5),
    NAME        VARCHAR2(50),
    JOIN_DATE   DATE,
    CREATED_AT  TIMESTAMP
);

DESC SAMPLE_TYPES;
```

---

## 6. CHAR vs VARCHAR2

> **TL;DR:** `CHAR` always uses its full fixed length (padding with spaces); `VARCHAR2` only uses as much space as the actual text needs. Default to `VARCHAR2`.

**CHAR** — fixed length, pads with spaces
```sql
CHAR(5)  'Ben'  →  'Ben  '
```

**VARCHAR2** — variable length, stores only required characters
```sql
VARCHAR2(5)  'Ben'  →  'Ben'
```

**Example** — proving the padding difference:
```sql
CREATE TABLE CHAR_TEST (
    C CHAR(10),
    V VARCHAR2(10)
);

INSERT INTO CHAR_TEST VALUES ('Ben', 'Ben');

SELECT LENGTH(C) AS CHAR_LEN, LENGTH(V) AS VARCHAR2_LEN
FROM CHAR_TEST;
-- CHAR_LEN = 10 (padded), VARCHAR2_LEN = 3 (exact)
```

 Use `VARCHAR2` for most text columns.

---

## 7. DATE vs TIMESTAMP

> **TL;DR:** `DATE` stores down to the second; `TIMESTAMP` also stores fractional (sub-second) precision.

**DATE** — Year, Month, Day, Hour, Minute, Second
```
28-JUL-2026 10:30:45
```

**TIMESTAMP** — everything in DATE + Fractional Seconds
```
28-JUL-2026 10:30:45.123456
```

**Example**
```sql
SELECT SYSDATE, SYSTIMESTAMP
FROM DUAL;
-- SYSDATE      -> 03-AUG-26
-- SYSTIMESTAMP -> 03-AUG-26 05.42.11.123456 AM +05:30
```

---

## 8. SQL Clause Execution Order

> **TL;DR:** SQL is *written* as SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY, but Oracle *executes* it FROM/WHERE first and SELECT/ORDER BY last.

```
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

**Example**
```sql
SELECT FIRST_NAME
FROM EMPLOYEES
WHERE SALARY > 5000
ORDER BY SALARY;
-- engine runs: FROM -> WHERE -> SELECT -> ORDER BY
```

---

## 9. Common Oracle Errors

> **TL;DR:** Most beginner errors come from typos in column/table names or broken SQL syntax — the error code tells you which.

| Error     | Meaning              | Example that triggers it |
|-----------|-----------------------|----------------------------|
| ORA-00904 | Invalid column         | `SELECT FIRST_NAM FROM EMPLOYEES;` |
| ORA-00942 | Table doesn't exist    | `SELECT * FROM EMPLOYEES;` |
| ORA-00936 | Missing expression     | `SELECT FROM EMPLOYEES;` |
| ORA-00933 | SQL syntax error       | `SELECT * FROM EMPLOYEES WHERE;` |
| ORA-01722 | Invalid number         | `SELECT * FROM EMPLOYEES WHERE SALARY = 'ABC';` |
| ORA-01400 | Cannot insert NULL     | `INSERT INTO EMPLOYEES (EMP_ID) VALUES (NULL);` *(on a NOT NULL column)* |

---

## 10. SELECT Statement

> **TL;DR:** `SELECT` picks which columns you want, `FROM` says which table to pull them from.

```sql
SELECT column_name
FROM table_name;
```

**Example**
```sql
SELECT *
FROM EMPLOYEES;

SELECT FIRST_NAME, SALARY
FROM EMPLOYEES;
```

---

## 11. DISTINCT

> **TL;DR:** Strips out duplicate rows from the result — considers ALL listed columns together, not one at a time.

```sql
SELECT DISTINCT FIRST_NAME
FROM EMPLOYEES;
-- 107 rows -> 91 distinct
```

**Example** — multi-column DISTINCT:
```sql
SELECT DISTINCT FIRST_NAME, LAST_NAME
FROM EMPLOYEES;
-- a row is only removed if BOTH first_name AND last_name repeat together
```

---

## 12. CONCAT / `||`

> **TL;DR:** Both glue strings together, but `CONCAT` only takes exactly 2 arguments while `||` can chain as many as you want.

```sql
SELECT FIRST_NAME || ' ' || LAST_NAME || '-' || SALARY
FROM EMPLOYEES;
```

**Example** — where `CONCAT` breaks and `||` doesn't:
```sql
SELECT CONCAT(FIRST_NAME, LAST_NAME)
FROM EMPLOYEES;                       --  works, 2 args

SELECT CONCAT(FIRST_NAME, LAST_NAME, SALARY)
FROM EMPLOYEES;                       --  ERROR: invalid number of arguments

SELECT FIRST_NAME || LAST_NAME || SALARY
FROM EMPLOYEES;                       --  works, unlimited args
```

---

## 13. Alias

> **TL;DR:** A temporary rename for a column or table, only for the duration of that query.

```sql
SELECT FIRST_NAME AS NAME, LAST_NAME FATHER_NAME
FROM EMPLOYEES;
```

**Example** — table alias used to shorten references:
```sql
SELECT E.FIRST_NAME, E.SALARY
FROM EMPLOYEES E
WHERE E.SALARY > 10000;
```

---

## 14. DUAL Table

> **TL;DR:** Oracle's built-in "scratchpad" table (1 row, 1 column) used to test expressions without needing a real table.

```sql
SELECT *
FROM DUAL;
```

**Example**
```sql
SELECT 10+2
FROM DUAL;             -- 12

SELECT 10, 'AIMORE'
FROM DUAL;
```

>  `SELECT 10+2 FROM EMPLOYEES;` runs once per row in EMPLOYEES — use `DUAL` instead for a single result.

---

## 15. ORDER BY

> **TL;DR:** Sorts the final result set; always the last clause in a query; ASC is the default direction.

```sql
SELECT * FROM EMPLOYEES ORDER BY SALARY ASC;
```

**Example** — multi-column sort:
```sql
SELECT *
FROM EMPLOYEES
ORDER BY DEPARTMENT_ID DESC, FIRST_NAME ASC;
-- sorts by department first (high to low), then name within each department (A-Z)
```

---

## 16. Relational Operators

> **TL;DR:** Operators used in `WHERE` to compare a column against a value or set of values.

| Operator     | Meaning                |
|--------------|--------------------------|
| =            | Equal                    |
| <> / !=      | Not Equal                 |
| >            | Greater Than              |
| <            | Less Than                 |
| >=           | Greater Than or Equal     |
| <=           | Less Than or Equal        |
| IN           | Match any value           |
| NOT IN       | Not in list                |
| BETWEEN      | Range                      |
| NOT BETWEEN  | Outside range              |
| IS NULL      | NULL values                |
| IS NOT NULL  | Not NULL                    |
| LIKE         | Pattern search              |
| NOT LIKE     | Opposite                    |

**Example** — one query touching several operators:
```sql
SELECT *
FROM EMPLOYEES
WHERE SALARY BETWEEN 10000 AND 17000
  AND EMPLOYEE_ID IN (100, 105, 110, 300)
  AND COMMISSION_PCT IS NULL;
```

>  NULL is an *undefined* value — use `IS NULL` / `IS NOT NULL`, never `= NULL`.

---

## 17. LIKE

> **TL;DR:** Pattern search on text — `%` matches any number of characters, `_` matches exactly one.

| Wildcard | Meaning                  |
|----------|----------------------------|
| `%`      | Zero or many characters     |
| `_`      | Exactly one character       |

**Example**
```sql
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE 'S%';     -- starts with S
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE '%n';     -- ends with n
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE '%MEN%';  -- contains MEN
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE '_a%';    -- 2nd letter is 'a'
SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE '___';    -- exactly 3 characters
```

---

## 18. Logical Operators

> **TL;DR:** `AND` needs every condition to be true; `OR` needs just one condition to be true.

| Operator | Combination      | Result |
|----------|-------------------|--------|
| AND      | TRUE AND TRUE      | Result |
| AND      | TRUE AND FALSE     | FALSE  |
| OR       | TRUE OR TRUE       | Result |
| OR       | TRUE OR FALSE      | Result |
| OR       | FALSE OR FALSE     | FALSE  |

**Example**
```sql
SELECT * FROM EMPLOYEES
WHERE FIRST_NAME = 'Steven' AND SALARY = 24000;  -- both must match

SELECT * FROM EMPLOYEES
WHERE FIRST_NAME = 'Steven' OR SALARY = 24000;   -- either can match
```

---

## 19. Single Row Functions

> **TL;DR:** Functions that transform ONE row's value at a time (as opposed to aggregate functions, which act across many rows).

```
Input: Steven → UPPER() → STEVEN
```

###  Number Functions

> **TL;DR:** Round, floor, ceil, truncate, or inspect the sign/remainder of numbers.

| Function | Purpose         | Example                          |
|----------|------------------|-----------------------------------|
| ROUND    | Round value       | `ROUND(10.45)` → `10`             |
| FLOOR    | Lower integer      | `FLOOR(10.999999)` → `10`         |
| CEIL     | Upper integer      | `CEIL(10.001)` → `11`             |
| MOD      | Remainder          | `MOD(10, 2)` → `0`                |
| ABS      | Absolute value     | `ABS(-3457)` → `3457`             |
| SIGN     | Sign of number     | `SIGN(-345678)` → `-1`            |
| TRUNC    | Remove decimals    | `TRUNC(15.4567, 2)` → `15.45`     |

**Example**
```sql
SELECT EMPLOYEE_ID, MOD(EMPLOYEE_ID, 2)
FROM EMPLOYEES
WHERE MOD(EMPLOYEE_ID, 2) = 1; -- odd employee IDs
```

###  Character Functions

> **TL;DR:** Reshape, search, pad, trim, or slice text values.

| Function  | Purpose                             |
|-----------|---------------------------------------|
| UPPER     | Uppercase                              |
| LOWER     | Lowercase                              |
| INITCAP   | First letter of each word uppercase     |
| LENGTH    | Count characters                        |
| REVERSE   | Reverse the string                      |
| REPLACE   | Replace a word/char with another        |
| TRANSLATE | Char-by-char replacement                |
| LPAD/RPAD | Pad left / pad right                    |
| TRIM      | Remove leading & trailing spaces        |
| LTRIM     | Remove left spaces                      |
| RTRIM     | Remove right spaces                     |
| INSTR     | Find position of a pattern              |
| SUBSTR    | Extract part of a string                |

**Example**
```sql
SELECT UPPER(FIRST_NAME), LOWER(FIRST_NAME), INITCAP(FIRST_NAME)
FROM EMPLOYEES;

SELECT REPLACE(FIRST_NAME, 'e', '*') FROM EMPLOYEES;
SELECT TRANSLATE('STEVEN', 'AEIOU', '12345') FROM DUAL;

SELECT LPAD(EMPLOYEE_ID, 6, '0') FROM EMPLOYEES;  -- '000101'
SELECT RPAD(EMPLOYEE_ID, 6, '0') FROM EMPLOYEES;  -- '101000'

SELECT TRIM('  steven  ') FROM DUAL;   -- 'steven'

-- SUBSTR(input, start_position, length)
SELECT SUBSTR('ORACLE DATABASE', 1, 3) FROM DUAL;   -- 'ORA'
SELECT SUBSTR('ORACLE DATABASE', 4, 7) FROM DUAL;   -- 'CLE DAT'
SELECT SUBSTR('ORACLE DATABASE', -5, 3) FROM DUAL;  -- 'ABA' (counts from end)

-- INSTR(input, pattern, start_position, occurrence)
SELECT INSTR('ORACLE DATABASE', 'A', 1, 2) FROM DUAL; -- position of 2nd 'A'
```

###  Date Functions

> **TL;DR:** Shift, compare, or snap dates to month/weekday boundaries.

| Function       | Purpose                |
|-----------------|--------------------------|
| ADD_MONTHS      | Add/subtract months       |
| MONTHS_BETWEEN  | Difference in months      |
| LAST_DAY        | Last day of the month      |
| NEXT_DAY        | Next given weekday         |

**Example**
```sql
SELECT SYSDATE, ADD_MONTHS(SYSDATE, -10) FROM DUAL;

SELECT FIRST_NAME, HIRE_DATE,
       ROUND(MONTHS_BETWEEN(SYSDATE, HIRE_DATE) / 12) AS YEARS_WORKED
FROM EMPLOYEES;

SELECT LAST_DAY(SYSDATE) FROM DUAL;
SELECT NEXT_DAY(SYSDATE, 'FRIDAY') FROM DUAL;
```

###  Data Type Conversion

> **TL;DR:** Convert values between text, number, and date so they can be compared or calculated correctly.

| Function  | Converts              |
|-----------|--------------------------|
| TO_NUMBER | String → Number           |
| TO_CHAR   | Number/Date → String       |
| TO_DATE   | String → Date               |
| CAST      | Convert any datatype        |

**Example**
```sql
SELECT TO_NUMBER('10') FROM DUAL;
SELECT TO_CHAR(SYSDATE, 'DD-MON-YYYY') FROM DUAL;
SELECT TO_CHAR(SYSDATE, 'DAY') FROM DUAL;
SELECT TO_DATE('15-06-2026', 'DD-MM-YYYY') FROM DUAL;

SELECT CAST('10' AS NUMBER) FROM DUAL;
SELECT CAST('10-12-2025' AS DATE) FROM DUAL;
SELECT CAST(65456 AS CHAR(10)) FROM DUAL;
```

###  General Functions

> **TL;DR:** Handle NULLs gracefully — substitute defaults, branch on null/not-null, or pick the first available value.

| Function | Purpose                | Syntax                                |
|----------|--------------------------|------------------------------------------|
| NVL      | Replace NULL              | `NVL(input, null_replace)`               |
| NVL2     | If NULL / Not NULL         | `NVL2(input, value_if_not_null, value_if_null)` |
| COALESCE | First non-NULL value       | `COALESCE(v1, v2, v3, ...)`              |
| NULLIF   | NULL if two values equal   | `NULLIF(a, b)`                            |

**Example**
```sql
SELECT COMMISSION_PCT, NVL(COMMISSION_PCT, 0)
FROM EMPLOYEES;

SELECT FIRST_NAME, SALARY,
       NVL2(COMMISSION_PCT, 0.1, 0.05) AS COMMISSION_RATE,
       SALARY + (SALARY * NVL2(COMMISSION_PCT, 0.1, 0.05)) AS FINAL_AMOUNT
FROM EMPLOYEES;

SELECT COALESCE(COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID)
FROM EMPLOYEES; -- returns first non-null column

SELECT NULLIF(10, 10) FROM DUAL; -- NULL
SELECT NULLIF(10, 20) FROM DUAL; -- 10
```

---

## 20. Set Operators

> **TL;DR:** Stack the results of two+ SELECTs on top of each other (not side by side) — column count & types must line up.

**Rules**
- Same number of columns in every SELECT
- Same (or compatible) data types in matching positions

| Operator   | Behavior                                 |
|------------|---------------------------------------------|
| UNION      | Merge rows, remove duplicates, sorted result |
| UNION ALL  | Merge rows, keep duplicates, no sorting       |
| INTERSECT  | Return only common rows                        |
| MINUS      | Return rows in first query but not the second   |

**Example**
```sql
-- T1: 1,2,3,4    T2: 3,4,5,6

SELECT * FROM T1
UNION
SELECT * FROM T2;
-- 1,2,3,4,5,6

SELECT * FROM T1
UNION ALL
SELECT * FROM T2;
-- 1,2,3,4,3,4,5,6

SELECT * FROM T1
INTERSECT
SELECT * FROM T2;
-- 3,4

SELECT * FROM T1
MINUS
SELECT * FROM T2;
-- 1,2
```

 Column count mismatch:
```sql
SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES WHERE DEPARTMENT_ID = 90
UNION
SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENT_ID IN (10,20,30);
--  ORA-00913 / query block has incorrect number of result columns
```

 Data type mismatch at a given position:
```sql
SELECT EMPLOYEE_ID, FIRST_NAME FROM EMPLOYEES WHERE DEPARTMENT_ID = 90
UNION
SELECT DEPARTMENT_NAME, DEPARTMENT_ID FROM DEPARTMENTS WHERE DEPARTMENT_ID IN (10,20,30);
--  expression must have same datatype as corresponding expression
-- (2nd column: VARCHAR2 vs NUMBER mismatch)
```

---

##  Mental Model

```
Database
│
├── Schema
│      │
│      ├── Table
│      ├── View
│      ├── Index
│      ├── MVIEW
│      └── GTT
│
└── Another Schema
```

```
EMPLOYEES
EMP_ID | FIRST_NAME | SALARY

EMP_ID         NUMBER
FIRST_NAME     VARCHAR2(50)
SALARY         NUMBER(10,2)
HIRE_DATE      DATE
```

---
