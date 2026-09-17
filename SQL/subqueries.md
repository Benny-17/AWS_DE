SUBQUERIES
----------

Subquery = query inside another query.

Purpose:
One query uses the result produced by another query.


1. SCALAR SUBQUERY
------------------
Usually used in SELECT.

Returns:
1 row + 1 column = 1 value.

Example:
SELECT employee_id,
       (SELECT AVG(salary) FROM employees)
FROM employees;


2. INLINE VIEW
--------------
Subquery used in FROM.

Acts like a temporary result set/table
for the outer query.


3. SUBQUERY IN WHERE
--------------------
Used when WHERE condition depends
on the result of another query.


SUBQUERY TYPES
--------------

4. SINGLE-ROW SUBQUERY
----------------------
Returns only one row.

Usually used with:
=
>
<
>=
<=
<>


5. MULTI-ROW SUBQUERY
---------------------
Returns multiple rows.

Common operators:
IN
ANY
ALL


6. MULTI-COLUMN SUBQUERY
------------------------
Returns multiple columns.

Used to compare multiple values/columns.


7. CORRELATED SUBQUERY
----------------------
Inner query depends on the outer query.


8. NESTED SUBQUERY
------------------
A subquery inside another subquery/query.


SUBQUERY OPERATORS
------------------

IN
→ Match a value against a list/result set.

EXISTS
→ Checks whether at least one matching row exists.

NOT EXISTS
→ Checks whether no matching row exists.

ANY
→ Condition must be true for at least ONE
   value returned by the subquery.

ALL
→ Condition must be true for EVERY
   value returned by the subquery.