# 1. SQL Basics

## 1.1 DDL — Data Definition Language

### What is DDL?

DDL is used to **create or modify the structure of database objects**.

Common DDL commands:

* `CREATE`
* `ALTER`
* `DROP`
* `TRUNCATE`

### Why do we use it?

We use DDL when we want to work with the **structure** of a database object such as a table.

### Syntax

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype
);
```

### Example

```sql
CREATE TABLE employees (
    employee_id NUMBER,
    employee_name VARCHAR2(100),
    salary NUMBER
);
```

### Explanation

This creates a table named `employees`.

The table contains:

```text
employee_id
employee_name
salary
```

`CREATE TABLE` creates the structure. It does not insert employee records.

---

## ALTER

Used to modify an existing object's structure.

```sql
ALTER TABLE employees
ADD department_id NUMBER;
```

This adds a new column.

---

## DROP

Used to remove an object completely.

```sql
DROP TABLE employees;
```

The table itself is removed.

---

## TRUNCATE

Used to remove all rows from a table.

```sql
TRUNCATE TABLE employees;
```

The table structure remains, but all rows are removed.

### Interview Cheat Sheet

| Command  | Purpose          |
| -------- | ---------------- |
| CREATE   | Create object    |
| ALTER    | Modify structure |
| DROP     | Remove object    |
| TRUNCATE | Remove all rows  |

### Important

`DELETE` is DML.

`TRUNCATE` is DDL.

---

# 1.2 DML — Data Manipulation Language

### What is DML?

DML is used to **insert, modify, and delete data**.

Common commands:

* `INSERT`
* `UPDATE`
* `DELETE`
* `MERGE`

### Why?

Because DML works with the **data inside tables**.

### INSERT

```sql
INSERT INTO employees
(employee_id, employee_name, salary)
VALUES
(101, 'Benny', 50000);
```

### Explanation

A new row is inserted into `employees`.

---

### UPDATE

```sql
UPDATE employees
SET salary = 60000
WHERE employee_id = 101;
```

The salary of employee `101` changes to `60000`.

---

### DELETE

```sql
DELETE FROM employees
WHERE employee_id = 101;
```

The matching row is deleted.

### Interview Cheat Sheet

```text
DDL → structure
DML → data
```

---

# 1.3 DQL — Data Query Language

### What is DQL?

DQL is used to **retrieve data**.

The main command is:

```sql
SELECT
```

### Example

```sql
SELECT employee_name, salary
FROM employees;
```

This retrieves employee names and salaries.

---

# 1.4 DCL — Data Control Language

### What is DCL?

DCL controls **permissions/access**.

Common commands:

```sql
GRANT
REVOKE
```

### Example

```sql
GRANT SELECT ON employees TO user1;
```

`user1` receives permission to read the table.

---

# 1.5 TCL — Transaction Control Language

### What is TCL?

TCL controls database transactions.

Common commands:

```sql
COMMIT
ROLLBACK
SAVEPOINT
```

### Example

```sql
UPDATE employees
SET salary = 70000
WHERE employee_id = 101;

ROLLBACK;
```

The update is undone if it has not been committed.

---

# 2. Database Objects

## 2.1 TABLE

### What is a table?

A table stores data in:

```text
Rows + Columns
```

### Why?

Tables are the primary objects used to store structured data.

### Syntax

```sql
CREATE TABLE employees (
    employee_id NUMBER,
    employee_name VARCHAR2(100),
    salary NUMBER
);
```

---

# 2.2 VIEW

### What is a View?

A View is a **stored SQL query** that behaves like a virtual table.

Normally, a view does not store the actual result data.

### Why?

* Simplify complex queries
* Provide security
* Hide unnecessary columns
* Reuse queries

### Syntax

```sql
CREATE VIEW employee_view AS
SELECT employee_id, employee_name, salary
FROM employees;
```

### Example

```sql
SELECT *
FROM employee_view;
```

### Explanation

Instead of repeatedly writing:

```sql
SELECT employee_id, employee_name, salary
FROM employees;
```

we can simply use:

```sql
SELECT *
FROM employee_view;
```

### Interview

> View = stored query / virtual table.

---

# 2.3 MATERIALIZED VIEW

### What is it?

A Materialized View stores the **result of a query physically**.

Unlike a normal View, the result is stored.

### Why?

Mainly for:

* Faster reporting
* Performance improvement
* Precomputed results

### Example

```sql
CREATE MATERIALIZED VIEW employee_summary
AS
SELECT department_id,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;
```

### Explanation

Oracle executes the query and stores the result.

Later:

```sql
SELECT *
FROM employee_summary;
```

does not need to calculate the original aggregation every time.

### View vs Materialized View

```text
VIEW
    ↓
Stores query

MATERIALIZED VIEW
    ↓
Stores query result
```

---

# 2.4 INDEX

### What is an Index?

An Index is a database structure used to **speed up data retrieval**.

Think of it like the index of a book.

Instead of checking every page:

```text
Find "Oracle"
    ↓
Book index
    ↓
Page 100
```

Similarly:

```text
WHERE employee_id = 101
        ↓
Index
        ↓
Find row faster
```

### Syntax

```sql
CREATE INDEX idx_emp_name
ON employees(employee_name);
```

### Why?

Without a suitable index, Oracle may need to scan many rows.

With an appropriate index, Oracle may be able to locate matching rows more efficiently.

### Important

An index does **not** contain the entire table.

It contains indexed values and information that helps Oracle locate the corresponding table rows.

---

# 2.5 GTT — Global Temporary Table

### What is it?

A Global Temporary Table is a table whose **data is temporary**, while its table definition remains available.

### Why?

Useful for:

* Temporary processing
* ETL
* Intermediate calculations
* Staging data

### Syntax

```sql
CREATE GLOBAL TEMPORARY TABLE temp_employees (
    employee_id NUMBER,
    salary NUMBER
);
```

### Example

```sql
INSERT INTO temp_employees
VALUES (101, 50000);
```

The data is temporary depending on the table's transaction/session definition.

---

# 2.6 EXTERNAL TABLE

### What is an External Table?

An external table allows Oracle to **read data stored outside the database**, such as a CSV file.

### Why?

Useful for:

* ETL
* Loading files
* Reading CSV files
* Data integration

Conceptually:

```text
CSV file
   ↓
External Table
   ↓
SELECT
```

The external file itself is not stored as normal table data inside Oracle.

---

# 3. Constraints

Constraints are rules used to maintain **data integrity**.

---

# 3.1 PRIMARY KEY

### What?

Uniquely identifies every row.

### Why?

A primary key:

* Must be unique
* Cannot contain NULL
* Identifies a row

### Example

```sql
CREATE TABLE employees (
    employee_id NUMBER PRIMARY KEY,
    employee_name VARCHAR2(100)
);
```

---

# 3.2 UNIQUE

### What?

Ensures values are unique.

```sql
CREATE TABLE employees (
    employee_id NUMBER,
    email VARCHAR2(100) UNIQUE
);
```

Two employees cannot have the same email.

### Primary Key vs Unique

```text
PRIMARY KEY
    ↓
Unique + NOT NULL
```

A table can have only one primary key constraint, while it can have multiple unique constraints.

---

# 3.3 NOT NULL

### What?

Prevents NULL values.

```sql
employee_name VARCHAR2(100) NOT NULL
```

---

# 3.4 CHECK

### What?

Ensures a condition is satisfied.

```sql
salary NUMBER CHECK (salary > 0)
```

---

# 3.5 FOREIGN KEY

### What?

Creates a relationship between tables.

### Example

```sql
CREATE TABLE departments (
    department_id NUMBER PRIMARY KEY
);
```

```sql
CREATE TABLE employees (
    employee_id NUMBER PRIMARY KEY,
    department_id NUMBER,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
```

### Explanation

`employees.department_id` references:

```text
departments.department_id
```

The parent value must exist before it can normally be referenced.

---

# 4. Data Types

Common Oracle data types:

| Data Type | Purpose                             |
| --------- | ----------------------------------- |
| NUMBER    | Numeric values                      |
| VARCHAR2  | Variable-length text                |
| CHAR      | Fixed-length text                   |
| DATE      | Date + time                         |
| TIMESTAMP | Date + time with fractional seconds |
| CLOB      | Large character data                |
| BLOB      | Binary data                         |

### Example

```sql
CREATE TABLE employees (
    employee_id NUMBER,
    employee_name VARCHAR2(100),
    gender CHAR(1),
    hire_date DATE,
    created_at TIMESTAMP
);
```

---

# 5. Basic SQL

## 5.1 SELECT

### What?

Retrieves columns/data.

### Syntax

```sql
SELECT column_name
FROM table_name;
```

### Example

```sql
SELECT employee_name, salary
FROM employees;
```

### Explanation

```text
SELECT
    ↓
Which columns?

FROM
    ↓
Which table?
```

---

# 5.2 WHERE

### What?

Filters rows.

### Syntax

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

Only employees with salary greater than `50000` are returned.

---

# 5.3 DISTINCT

### What?

Removes duplicate results.

```sql
SELECT DISTINCT department_id
FROM employees;
```

If department IDs are:

```text
10
10
20
20
30
```

Result:

```text
10
20
30
```

---

# 5.4 GROUP BY

### What?

Groups rows so aggregate functions can be applied.

### Example

```sql
SELECT department_id,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

### Explanation

Employees are grouped by department.

```text
Department 10 → 5 employees
Department 20 → 8 employees
Department 30 → 3 employees
```

---

# 5.5 HAVING

### What?

Filters groups created by `GROUP BY`.

```sql
SELECT department_id,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

### WHERE vs HAVING

```text
WHERE
    ↓
Filters rows

GROUP BY
    ↓
Creates groups

HAVING
    ↓
Filters groups
```

---

# 5.6 ORDER BY

### What?

Sorts the result.

```sql
SELECT employee_name, salary
FROM employees
ORDER BY salary DESC;
```

`DESC` = highest to lowest.

`ASC` = lowest to highest.

---

# SQL Logical Processing Order

A very important interview concept:

```text
FROM
 ↓
WHERE
 ↓
GROUP BY
 ↓
HAVING
 ↓
SELECT
 ↓
DISTINCT
 ↓
ORDER BY
```

Remember:

> Written order is not the same as logical execution order.

---

# 6. Operators

## 6.1 Relational Operators

```text
=
<>
!=
>
<
>=
<=
```

Example:

```sql
SELECT *
FROM employees
WHERE salary >= 50000;
```

---

# 6.2 Logical Operators

```text
AND
OR
NOT
```

Example:

```sql
SELECT *
FROM employees
WHERE salary > 50000
AND department_id = 10;
```

---

# 6.3 LIKE

Used for pattern matching.

```sql
SELECT *
FROM employees
WHERE employee_name LIKE 'A%';
```

Meaning:

> Names beginning with A.

Common wildcards:

```text
% → zero or more characters
_ → exactly one character
```

---

# 6.4 IN

Used to check multiple values.

```sql
SELECT *
FROM employees
WHERE department_id IN (10, 20, 30);
```

Equivalent idea:

```sql
department_id = 10
OR department_id = 20
OR department_id = 30
```

---

# 6.5 BETWEEN

Used for a range.

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 30000 AND 50000;
```

`BETWEEN` is inclusive of both boundaries.

---

# 6.6 NULL

NULL means **missing/unknown value**.

Do not use:

```sql
WHERE salary = NULL
```

Use:

```sql
WHERE salary IS NULL;
```

Or:

```sql
WHERE salary IS NOT NULL;
```

### Interview

```text
NULL is not equal to 0.
NULL is not an empty string conceptually.
NULL represents missing/unknown.
```

---

# 7. Functions

Functions perform operations on values.

Main categories:

```text
Number
Character
Date
Conversion
NULL / General
```

---

# 7.1 Number Functions

Examples:

```sql
ROUND(123.456, 2)
TRUNC(123.456, 2)
CEIL(123.2)
FLOOR(123.8)
MOD(10, 3)
```

Example:

```sql
SELECT ROUND(123.456, 2)
FROM dual;
```

Result:

```text
123.46
```

---

# 7.2 Character Functions

Common functions:

```sql
UPPER()
LOWER()
INITCAP()
LENGTH()
SUBSTR()
INSTR()
REPLACE()
TRIM()
```

Example:

```sql
SELECT UPPER(employee_name)
FROM employees;
```

---

# 7.3 Date Functions

Common functions:

```sql
SYSDATE
ADD_MONTHS()
MONTHS_BETWEEN()
NEXT_DAY()
LAST_DAY()
```

Example:

```sql
SELECT SYSDATE
FROM dual;
```

---

# 7.4 Conversion Functions

### TO_CHAR

Converts a value to character format.

```sql
SELECT TO_CHAR(SYSDATE, 'DD-MM-YYYY')
FROM dual;
```

### TO_DATE

Converts text into a date.

```sql
SELECT TO_DATE('27-08-2026', 'DD-MM-YYYY')
FROM dual;
```

### TO_NUMBER

Converts text into a number.

```sql
SELECT TO_NUMBER('5000')
FROM dual;
```

---

# 7.5 NULL / General Functions

Common functions:

```sql
NVL()
NVL2()
COALESCE()
NULLIF()
```

### NVL

```sql
SELECT NVL(commission, 0)
FROM employees;
```

If commission is NULL, return `0`.

### COALESCE

Returns the first non-NULL value.

```sql
SELECT COALESCE(phone, email, 'N/A')
FROM employees;
```

---

# 8. Aggregations

Aggregate functions operate on multiple rows.

```text
COUNT
SUM
AVG
MIN
MAX
```

---

## COUNT

```sql
SELECT COUNT(*)
FROM employees;
```

Counts rows.

### COUNT(column)

```sql
SELECT COUNT(commission)
FROM employees;
```

Counts non-NULL commission values.

### Important Interview Question

```text
COUNT(*)
```

counts rows.

```text
COUNT(column)
```

counts non-NULL values in that column.

---

## SUM

```sql
SELECT SUM(salary)
FROM employees;
```

---

## AVG

```sql
SELECT AVG(salary)
FROM employees;
```

---

## MIN / MAX

```sql
SELECT MIN(salary), MAX(salary)
FROM employees;
```

---

# 9. Joins

### What is a Join?

A Join combines data from multiple tables using a relationship/condition.

Example:

```text
EMPLOYEES
department_id

       ↓

DEPARTMENTS
department_id
```

---

# 9.1 INNER JOIN

Returns matching rows from both tables.

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;
```

### Think

```text
A ∩ B
```

Only matching records.

---

# 9.2 LEFT JOIN

Returns:

* All rows from left table
* Matching rows from right table

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id;
```

If there is no matching department:

```text
department_name = NULL
```

---

# 9.3 RIGHT JOIN

Returns all rows from the right table.

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id;
```

---

# 9.4 FULL OUTER JOIN

Returns:

```text
Matching rows
+
Unmatched rows from left
+
Unmatched rows from right
```

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.department_id = d.department_id;
```

---

# 9.5 CROSS JOIN

Returns every possible combination.

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
CROSS JOIN departments d;
```

If:

```text
Employees = 5 rows
Departments = 3 rows
```

Result:

```text
5 × 3 = 15 rows
```

---

# 9.6 SELF JOIN

A table joins with itself.

Common example:

```text
Employee
    ↓
Manager
```

```sql
SELECT e.employee_name AS employee,
       m.employee_name AS manager
FROM employees e
JOIN employees m
    ON e.manager_id = m.employee_id;
```

---

# 9.7 SEMI JOIN

Returns rows from one table when a match exists in another table.

Usually implemented using `EXISTS` or `IN`.

```sql
SELECT *
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.department_id = e.department_id
);
```

The important point:

> We only return rows from `employees`.

---

# 9.8 ANTI JOIN

Returns rows where no matching record exists.

Usually implemented using `NOT EXISTS`.

```sql
SELECT *
FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.department_id = e.department_id
);
```

### Interview Cheat Sheet

```text
INNER → matching

LEFT → everything from left

RIGHT → everything from right

FULL → everything from both

CROSS → every combination

SELF → table joins itself

SEMI → matching existence

ANTI → non-matching existence
```

---

# 10. Set Operators

Set operators combine results of multiple `SELECT` statements.

```text
UNION
UNION ALL
INTERSECT
MINUS
```

The queries must have compatible numbers/types of columns.

---

# 10.1 UNION

Combines results and removes duplicates.

```sql
SELECT department_id FROM employees
UNION
SELECT department_id FROM departments;
```

---

# 10.2 UNION ALL

Combines results and keeps duplicates.

```sql
SELECT department_id FROM employees
UNION ALL
SELECT department_id FROM departments;
```

### UNION vs UNION ALL

```text
UNION
→ removes duplicates
→ usually more work

UNION ALL
→ keeps duplicates
→ generally faster
```

---

# 10.3 INTERSECT

Returns values existing in both result sets.

```sql
SELECT department_id FROM employees
INTERSECT
SELECT department_id FROM departments;
```

---

# 10.4 MINUS

Oracle's set operator for finding rows in the first query that are not in the second.

```sql
SELECT department_id FROM departments
MINUS
SELECT department_id FROM employees;
```

---

# 11. Subqueries

### What is a Subquery?

A subquery is a **query inside another query**.

```text
Outer Query
    ↓
Inner Query
```

---

# 11.1 Scalar Subquery

Returns exactly one value.

### Example

Find employees earning more than the average salary:

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### Explanation

Inner query:

```sql
SELECT AVG(salary)
FROM employees
```

returns one value.

Example:

```text
50000
```

Then:

```sql
WHERE salary > 50000
```

is applied by the outer query.

---

# 11.2 Inline View

A subquery in the `FROM` clause.

```sql
SELECT *
FROM (
    SELECT department_id,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
);
```

The inner query behaves like a temporary result set/table for the outer query.

---

# 11.3 Nested Subquery

A subquery used inside another SQL statement, commonly in `WHERE`.

```sql
SELECT *
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location_id = 100
);
```

---

# 11.4 Correlated Subquery

The inner query depends on the current row of the outer query.

Example:

Find employees earning more than their department average.

```sql
SELECT e.employee_name,
       e.salary,
       e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

### Key idea

The inner query refers to:

```sql
e.department_id
```

from the outer query.

---

# 11.5 Non-Correlated Subquery

The inner query does not depend on the outer query.

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### Interview

```text
Correlated
→ inner query depends on outer query

Non-correlated
→ inner query is independent
```

---

# 12. CTE

CTE = Common Table Expression.

### What?

A named temporary result set created using `WITH`.

### Why?

Used to:

* Make queries readable
* Break complex queries into steps
* Reuse intermediate results
* Simplify debugging

### Syntax

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT *
FROM cte_name;
```

### Example

```sql
WITH dept_salary AS (
    SELECT department_id,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT *
FROM dept_salary
WHERE avg_salary > 50000;
```

### Explanation

Step 1:

```sql
WITH dept_salary AS (...)
```

creates the intermediate result.

Step 2:

```sql
SELECT *
FROM dept_salary
```

uses it.

---

# Recursive CTE

Used when data has a hierarchical or recursive relationship.

Examples:

```text
Employee → Manager → Manager
Category → Subcategory → Subcategory
Parent → Child
```

Conceptually:

```text
Anchor query
     ↓
Recursive query
     ↓
Next level
     ↓
Next level
```

Oracle supports recursive hierarchy techniques and recursive subquery factoring.

---

# 13. Analytical / Window Functions

### What?

Window functions calculate values across related rows **without collapsing the rows**.

This is the major difference between:

```text
GROUP BY
```

and:

```text
WINDOW FUNCTION
```

### Example

```sql
SELECT employee_name,
       salary,
       AVG(salary) OVER () AS company_avg
FROM employees;
```

Every employee row remains.

---

# OVER()

`OVER()` tells Oracle that a function should operate as a window function.

```sql
AVG(salary) OVER ()
```

means:

> Calculate the average across the selected window while keeping each row.

---

# PARTITION BY

Divides rows into groups/windows.

```sql
AVG(salary) OVER (
    PARTITION BY department_id
)
```

Meaning:

> Calculate the average salary separately for each department.

---

# 13.1 ROW_NUMBER

Assigns a unique sequential number.

```sql
SELECT employee_name,
       salary,
       ROW_NUMBER() OVER (
           ORDER BY salary DESC
       ) AS rn
FROM employees;
```

Example:

```text
salary    row_number

100000       1
90000        2
90000        3
80000        4
```

Every row gets a different number.

---

# 13.2 RANK

Same values receive the same rank, with gaps.

```sql
SELECT salary,
       RANK() OVER (
           ORDER BY salary DESC
       ) AS rnk
FROM employees;
```

Example:

```text
100000 → 1
90000  → 2
90000  → 2
80000  → 4
```

---

# 13.3 DENSE_RANK

Same values receive the same rank, but there are no gaps.

```text
100000 → 1
90000  → 2
90000  → 2
80000  → 3
```

### Most important comparison

```text
ROW_NUMBER
1
2
3
4

RANK
1
2
2
4

DENSE_RANK
1
2
2
3
```

---

# 13.4 LAG

Gets a previous row's value.

```sql
SELECT employee_id,
       salary,
       LAG(salary) OVER (
           ORDER BY employee_id
       ) AS previous_salary
FROM employees;
```

Useful for:

* Comparing current vs previous
* Change detection
* Time-series analysis

---

# 13.5 LEAD

Gets the next row's value.

```sql
SELECT employee_id,
       salary,
       LEAD(salary) OVER (
           ORDER BY employee_id
       ) AS next_salary
FROM employees;
```

---

# 13.6 NTILE

Divides rows into approximately equal groups.

```sql
SELECT employee_name,
       salary,
       NTILE(4) OVER (
           ORDER BY salary DESC
       ) AS bucket
FROM employees;
```

Creates four buckets.

---

# 13.7 Running Total

```sql
SELECT employee_id,
       salary,
       SUM(salary) OVER (
           ORDER BY employee_id
           ROWS BETWEEN UNBOUNDED PRECEDING
           AND CURRENT ROW
       ) AS running_total
FROM employees;
```

Concept:

```text
Row 1 → salary1
Row 2 → salary1 + salary2
Row 3 → salary1 + salary2 + salary3
```

---

# 13.8 Window Aggregates

Aggregate functions can also be window functions.

```sql
SUM(salary) OVER (...)
AVG(salary) OVER (...)
COUNT(*) OVER (...)
MIN(salary) OVER (...)
MAX(salary) OVER (...)
```

### GROUP BY vs Window Function

`GROUP BY`:

```text
10 employees
    ↓
1 group result
```

Window function:

```text
10 employees
    ↓
10 rows remain
+ calculated value
```

---

# 14. CASE

### What?

`CASE` performs conditional logic.

It is similar to:

```text
IF / ELSE IF / ELSE
```

### Syntax

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

### Example

```sql
SELECT employee_name,
       salary,
       CASE
           WHEN salary >= 100000 THEN 'HIGH'
           WHEN salary >= 50000 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS salary_category
FROM employees;
```

### Explanation

```text
salary >= 100000 → HIGH

salary >= 50000 → MEDIUM

otherwise → LOW
```

---

# 15. Advanced GROUP BY

## 15.1 ROLLUP

Used to generate subtotals and grand totals.

```sql
SELECT department_id,
       job_id,
       SUM(salary)
FROM employees
GROUP BY ROLLUP(department_id, job_id);
```

Conceptually:

```text
Department + Job
Department subtotal
Grand total
```

---

# 15.2 CUBE

Generates combinations of grouping columns.

```sql
SELECT department_id,
       job_id,
       SUM(salary)
FROM employees
GROUP BY CUBE(department_id, job_id);
```

Useful for multidimensional reporting.

---

# 15.3 GROUPING SETS

Allows you to explicitly specify which groups you want.

```sql
SELECT department_id,
       job_id,
       SUM(salary)
FROM employees
GROUP BY GROUPING SETS (
    (department_id),
    (job_id),
    ()
);
```

`()` represents the grand total.

### Cheat Sheet

```text
ROLLUP
→ hierarchical subtotals + total

CUBE
→ combinations of dimensions

GROUPING SETS
→ explicitly choose grouping combinations
```

---

# 16. MERGE

### What?

`MERGE` performs an **INSERT or UPDATE depending on whether a matching row exists**.

This is commonly called an **upsert**.

### Why?

Useful in:

* ETL
* Data Warehousing
* Synchronizing tables
* Loading changed data

### Example

```sql
MERGE INTO employees e
USING employee_stage s
ON (e.employee_id = s.employee_id)

WHEN MATCHED THEN
    UPDATE SET
        e.salary = s.salary

WHEN NOT MATCHED THEN
    INSERT (employee_id, employee_name, salary)
    VALUES (s.employee_id, s.employee_name, s.salary);
```

### Explanation

If employee exists:

```text
MATCHED
    ↓
UPDATE
```

If employee doesn't exist:

```text
NOT MATCHED
    ↓
INSERT
```

### Interview

> MERGE = commonly used for UPSERT operations.

---

# 17. Indexes

Indexes are used to improve data retrieval performance.

---

# 17.1 Unique Index

Does not allow duplicate indexed values.

```sql
CREATE UNIQUE INDEX idx_emp_email
ON employees(email);
```

---

# 17.2 Non-Unique Index

Allows duplicate values.

```sql
CREATE INDEX idx_emp_dept
ON employees(department_id);
```

Multiple employees can belong to the same department.

---

# 17.3 B-tree Index

The common general-purpose index structure.

Useful for columns with many different values and common equality/range searches.

Example:

```sql
CREATE INDEX idx_emp_salary
ON employees(salary);
```

---

# 17.4 Bitmap Index

Stores bitmap representations for column values.

Often useful in Oracle data warehouse environments for columns with relatively low cardinality.

Example:

```sql
CREATE BITMAP INDEX idx_emp_gender
ON employees(gender);
```

Typical candidates can include columns such as:

```text
Gender
Status
Region
```

depending on workload.

---

# 17.5 Function-Based Index

Index based on an expression/function.

Example:

```sql
CREATE INDEX idx_emp_upper_name
ON employees(UPPER(employee_name));
```

Now a query such as:

```sql
SELECT *
FROM employees
WHERE UPPER(employee_name) = 'BENNY';
```

can potentially benefit from that index.

---

# 17.6 Composite Index

Index on multiple columns.

```sql
CREATE INDEX idx_emp_dept_salary
ON employees(department_id, salary);
```

This is a two-column index.

### Important

Column order matters.

```text
(department_id, salary)
```

is not automatically equivalent to:

```text
(salary, department_id)
```

---

# Primary Key / Unique Constraint and Index

Oracle commonly creates a unique index to support a primary key or unique constraint, unless an appropriate existing index is used/configured.

Important distinction:

```text
Constraint
→ enforces a rule

Index
→ provides an access structure
```

---

# 18. Query Optimization

## What is Query Optimization?

Query optimization is the process of making SQL queries execute efficiently.

The goal is usually to reduce:

* I/O
* CPU
* Memory usage
* Execution time

---

# 18.1 EXPLAIN PLAN

### What?

Shows the execution plan Oracle expects to use.

### Example

```sql
EXPLAIN PLAN FOR
SELECT *
FROM employees
WHERE employee_id = 101;
```

Then:

```sql
SELECT *
FROM TABLE(DBMS_XPLAN.DISPLAY);
```

---

# 18.2 Full Table Scan

Oracle reads many/all blocks of a table.

Conceptually:

```text
TABLE
 ↓
Read many blocks
 ↓
Check rows
```

A full table scan is not automatically bad.

For a small table, it may be the best option.

---

# 18.3 Index Scan

Oracle can use an index to locate rows.

Conceptually:

```text
Query
 ↓
Index
 ↓
Row location
 ↓
Table row
```

Whether an index is beneficial depends on the query, table size, selectivity, statistics, and other factors.

---

# 18.4 Execution Plan

The execution plan describes how Oracle intends to execute a query.

Example operations can include:

```text
TABLE ACCESS FULL
INDEX RANGE SCAN
INDEX UNIQUE SCAN
HASH JOIN
NESTED LOOPS
SORT
```

### Interview Point

Never say:

> "Index is always faster."

Correct answer:

> "Oracle's optimizer chooses an execution plan based on factors such as statistics, predicates, selectivity, available indexes, and estimated cost."

---

# 19. SQL Problem Solving

This section contains common SQL interview patterns.

---

# 19.1 Find Duplicates

Example: find duplicate salaries.

```sql
SELECT salary,
       COUNT(*) AS cnt
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1;
```

### Pattern

```text
GROUP BY
+
HAVING COUNT(*) > 1
```

---

# 19.2 Remove Duplicates

One common approach is `ROW_NUMBER()`.

```sql
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY employee_name, salary
               ORDER BY employee_id
           ) AS rn
    FROM employees e
)
WHERE rn = 1;
```

For an actual `DELETE`, use a carefully designed duplicate-identification strategy and verify the result before deleting.

---

# 19.3 Nth Highest Salary

Example: second highest salary.

```sql
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (
               ORDER BY salary DESC
           ) AS rnk
    FROM employees
)
WHERE rnk = 2;
```

### Why DENSE_RANK?

If salaries are:

```text
100000
90000
90000
80000
```

Then:

```text
100000 → 1
90000  → 2
90000  → 2
80000  → 3
```

---

# 19.4 Top N Per Group

Example:

> Find the top 3 salaries in each department.

```sql
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rn
    FROM employees e
)
WHERE rn <= 3;
```

### Pattern

```text
PARTITION BY group
+
ORDER BY ranking_column
+
ROW_NUMBER / RANK / DENSE_RANK
```

---

# 19.5 Missing Records

Example:

Find departments that have no employees.

```sql
SELECT d.department_id
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;
```

Another common approach:

```sql
SELECT d.department_id
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.department_id
);
```

---

# 19.6 Gaps

Example:

Employee IDs:

```text
1
2
3
5
6
```

`4` is missing.

A common technique is to generate a sequence and compare it against the existing data.

Oracle example:

```sql
SELECT LEVEL AS id
FROM dual
CONNECT BY LEVEL <= 10;
```

Then compare generated IDs with the actual table.

---

# 19.7 Running Total

```sql
SELECT employee_id,
       salary,
       SUM(salary) OVER (
           ORDER BY employee_id
       ) AS running_total
FROM employees;
```

---

# 19.8 Latest Record

Suppose an employee has multiple records.

Use:

```sql
ROW_NUMBER()
```

Example:

```sql
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY employee_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM employee_history e
)
WHERE rn = 1;
```

### Meaning

For every employee:

```text
Latest record → rn = 1
Older record  → rn = 2
Older record  → rn = 3
```

---

# 19.9 Date Problems

### Employees who joined on Saturday/Sunday

Oracle:

```sql
SELECT *
FROM employees
WHERE TRUNC(hire_date) - TRUNC(hire_date, 'IW') + 1 IN (6, 7);
```

The expression identifies Saturday/Sunday using ISO week positioning.

---

### First day of current month

```sql
SELECT TRUNC(SYSDATE, 'MM')
FROM dual;
```

---

### Last day of current month

```sql
SELECT LAST_DAY(SYSDATE)
FROM dual;
```

---

### Next 5 days

```sql
SELECT SYSDATE + LEVEL
FROM dual
CONNECT BY LEVEL <= 5;
```

---

# 19.10 ETL-Style Problems

SQL is heavily used in ETL/Data Engineering.

Typical flow:

```text
Source
  ↓
Extract
  ↓
Stage
  ↓
Transform
  ↓
Validate
  ↓
Load
  ↓
Target
```

Typical SQL tasks:

```text
Remove duplicates
      ↓
Handle NULLs
      ↓
Transform columns
      ↓
Join reference data
      ↓
Calculate derived columns
      ↓
Find latest records
      ↓
Load target
```

Example:

```sql
INSERT INTO employee_target (
    employee_id,
    employee_name,
    salary
)
SELECT employee_id,
       UPPER(employee_name),
       NVL(salary, 0)
FROM employee_stage;
```

Here:

```text
UPPER()
→ transforms the name

NVL()
→ handles NULL salary

SELECT
→ reads staging data

INSERT
→ loads target data
```

---

# SQL Interview Cheat Sheet

## SQL Command Categories

```text
DDL
→ CREATE
→ ALTER
→ DROP
→ TRUNCATE

DML
→ INSERT
→ UPDATE
→ DELETE
→ MERGE

DQL
→ SELECT

DCL
→ GRANT
→ REVOKE

TCL
→ COMMIT
→ ROLLBACK
→ SAVEPOINT
```

---

# Database Objects

```text
TABLE
→ Stores data

VIEW
→ Stores query definition

MATERIALIZED VIEW
→ Stores query result

INDEX
→ Helps data retrieval

GTT
→ Temporary data

EXTERNAL TABLE
→ Reads external files
```

---

# Constraints

```text
PRIMARY KEY
→ Unique + NOT NULL

UNIQUE
→ Prevents duplicate values

NOT NULL
→ Value required

CHECK
→ Condition/rule

FOREIGN KEY
→ Relationship between tables
```

---

# Filtering

```text
WHERE
→ Filters rows

HAVING
→ Filters groups
```

---

# Aggregation

```text
COUNT
SUM
AVG
MIN
MAX
```

Remember:

```sql
GROUP BY
```

reduces rows into groups.

---

# Joins

```text
INNER
→ matching rows

LEFT
→ all left + matching right

RIGHT
→ all right + matching left

FULL
→ all rows from both

CROSS
→ every combination

SELF
→ table joins itself

SEMI
→ match exists

ANTI
→ match does not exist
```

---

# Set Operators

```text
UNION
→ combines + removes duplicates

UNION ALL
→ combines + keeps duplicates

INTERSECT
→ common rows

MINUS
→ first result minus second result
```

---

# Subqueries

```text
Scalar
→ one value

Inline View
→ subquery in FROM

Nested
→ query inside another query

Correlated
→ inner query depends on outer query

Non-correlated
→ inner query is independent
```

---

# Window Functions

```text
ROW_NUMBER
→ unique sequence

RANK
→ same rank + gaps

DENSE_RANK
→ same rank + no gaps

LAG
→ previous row

LEAD
→ next row

NTILE
→ divide rows into buckets

SUM() OVER
→ running/window calculation

AVG() OVER
→ window average
```

---

# GROUP BY Extensions

```text
ROLLUP
→ subtotals + grand total

CUBE
→ combinations + totals

GROUPING SETS
→ custom grouping combinations
```

---

# Indexes

```text
UNIQUE
NON-UNIQUE
B-TREE
BITMAP
FUNCTION-BASED
COMPOSITE
```

Remember:

> An index is an access structure, not a copy of the entire table.

---

# Most Important Interview Differences

## DELETE vs TRUNCATE vs DROP

```text
DELETE
→ removes rows
→ DML
→ WHERE can be used

TRUNCATE
→ removes all rows
→ DDL
→ WHERE cannot be used

DROP
→ removes the object itself
```

---

## WHERE vs HAVING

```text
WHERE
→ filters rows before grouping

HAVING
→ filters groups after grouping
```

---

## UNION vs UNION ALL

```text
UNION
→ removes duplicates

UNION ALL
→ keeps duplicates
→ generally more efficient
```

---

## RANK vs DENSE_RANK vs ROW_NUMBER

For:

```text
100
90
90
80
```

Result:

```text
ROW_NUMBER    RANK    DENSE_RANK
-----------   ----    ----------
1             1       1
2             2       2
3             2       2
4             4       3
```

---

## GROUP BY vs Window Function

```text
GROUP BY
→ collapses rows

WINDOW FUNCTION
→ keeps rows
→ calculates additional information
```

---

## VIEW vs MATERIALIZED VIEW

```text
VIEW
→ query definition

MATERIALIZED VIEW
→ stored query result
```

---

## PRIMARY KEY vs UNIQUE

```text
PRIMARY KEY
→ uniquely identifies rows
→ cannot be NULL
→ one primary key constraint per table

UNIQUE
→ prevents duplicate values
→ NULL handling differs from primary key
→ multiple unique constraints can exist
```

---

## JOIN vs SUBQUERY

A JOIN combines data from tables/result sets.

A subquery provides a result to another query.

Both can often solve the same problem.

Choose based on:

```text
Readability
Performance
Query requirement
Optimizer behavior
```

---

# SQL Query Building Mental Model

When you see a SQL problem, ask:

### Step 1 — What data?

```sql
SELECT
```

### Step 2 — From where?

```sql
FROM
```

### Step 3 — Which rows?

```sql
WHERE
```

### Step 4 — Need groups?

```sql
GROUP BY
```

### Step 5 — Filter groups?

```sql
HAVING
```

### Step 6 — Need sorting?

```sql
ORDER BY
```

### Step 7 — Need another table?

```sql
JOIN
```

### Step 8 — Need a query inside another query?

```sql
SUBQUERY / CTE
```

### Step 9 — Need ranking/comparison without losing rows?

```sql
WINDOW FUNCTION
```

---

# Most Important SQL Patterns to Memorize

## Find duplicates

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > 1;
```

## Find Nth highest

```sql
SELECT *
FROM (
    SELECT t.*,
           DENSE_RANK() OVER (
               ORDER BY salary DESC
           ) AS rnk
    FROM employees t
)
WHERE rnk = N;
```

## Top N per group

```sql
SELECT *
FROM (
    SELECT t.*,
           ROW_NUMBER() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS rn
    FROM employees t
)
WHERE rn <= N;
```

## Latest record per group

```sql
SELECT *
FROM (
    SELECT t.*,
           ROW_NUMBER() OVER (
               PARTITION BY employee_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM employee_history t
)
WHERE rn = 1;
```

## Find records with no match

```sql
SELECT a.*
FROM table_a a
WHERE NOT EXISTS (
    SELECT 1
    FROM table_b b
    WHERE b.id = a.id
);
```

## Running total

```sql
SELECT id,
       amount,
       SUM(amount) OVER (
           ORDER BY id
       ) AS running_total
FROM transactions;
```

## Previous row

```sql
LAG(column_name) OVER (
    ORDER BY column_name
)
```

## Next row

```sql
LEAD(column_name) OVER (
    ORDER BY column_name
)
```

---

# Final SQL Learning Order

Use this order while studying:

```text
1. SQL Basics
       ↓
2. Database Objects
       ↓
3. Constraints
       ↓
4. Data Types
       ↓
5. SELECT / FROM / WHERE
       ↓
6. Operators
       ↓
7. Functions
       ↓
8. Aggregations
       ↓
9. Joins
       ↓
10. Set Operators
       ↓
11. Subqueries
       ↓
12. CTE
       ↓
13. Analytical / Window Functions
       ↓
14. CASE
       ↓
15. Advanced GROUP BY
       ↓
16. MERGE
       ↓
17. Indexes
       ↓
18. Query Optimization
       ↓
19. SQL Problem Solving
```

# Golden Rule for SQL Interviews

Don't just memorize:

```sql
SELECT
FROM
WHERE
```

Understand what each part does:

```text
SELECT
"What do I want?"

FROM
"Where is the data?"

WHERE
"Which rows do I need?"

GROUP BY
"How should I group the rows?"

HAVING
"Which groups do I need?"

JOIN
"Where is the related data?"

SUBQUERY / CTE
"Do I need an intermediate result?"

WINDOW FUNCTION
"Do I need calculations while keeping every row?"

ORDER BY
"How should I display the result?"
```

> **SQL interview success = understanding the problem + choosing the correct SQL pattern + writing clean syntax.**
