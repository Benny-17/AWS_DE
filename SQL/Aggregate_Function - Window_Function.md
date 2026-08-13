## 1. Aggregate / Group Functions

Aggregate functions calculate a value from **multiple rows** and return a summary.

### Aggregate Functions Covered

```sql
MIN()
MAX()
SUM()
AVG()
COUNT()
```

Example:

```sql
SELECT MIN(SALARY),
       MAX(SALARY),
       SUM(SALARY),
       COUNT(SALARY),
       AVG(SALARY)
FROM EMPLOYEES;
```

### COUNT()

```sql
COUNT(*)
```

→ Counts **all rows**

```sql
COUNT(COLUMN_NAME)
```

→ Counts **non-NULL values**

```sql
COUNT(1)
```

→ Counts rows

---

## 2. GROUP BY

`GROUP BY` is used when we want to calculate an aggregate **separately for each group**.

Example:

```sql
SELECT DEPARTMENT_ID,
       COUNT(*),
       MIN(SALARY),
       SUM(SALARY)
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;
```

Concept:

```text
EMPLOYEES
    ↓
GROUP BY DEPARTMENT_ID
    ↓
Department 10
Department 20
Department 30
    ↓
Aggregate calculation for each group
```

### Without GROUP BY

```sql
SELECT SUM(SALARY)
FROM EMPLOYEES;
```

→ Summary for the **whole table**

### With GROUP BY

```sql
SELECT DEPARTMENT_ID, SUM(SALARY)
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;
```

→ Summary **for each department**

---

## 3. WHERE with GROUP BY

`WHERE` filters **individual rows before grouping**.

```sql
SELECT DEPARTMENT_ID,
       COUNT(*),
       MIN(SALARY),
       SUM(SALARY)
FROM EMPLOYEES
WHERE DEPARTMENT_ID IN (10, 20, 30, 50, 90)
GROUP BY DEPARTMENT_ID;
```

Logical flow:

```text
FROM
 ↓
WHERE       → filter rows
 ↓
GROUP BY    → create groups
 ↓
Aggregate  → calculate
```

---

## 4. HAVING

`HAVING` filters **groups after aggregation**.

❌ Aggregate functions cannot be used in `WHERE`:

```sql
WHERE SUM(SALARY) > 50000
```

✅ Use `HAVING`:

```sql
SELECT DEPARTMENT_ID,
       COUNT(*),
       MIN(SALARY),
       SUM(SALARY)
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING SUM(SALARY) > 50000;
```

### Remember

```text
WHERE
→ filters ROWS

HAVING
→ filters GROUPS
```

---

## 5. Finding Duplicates

A common duplicate-finding pattern:

```sql
SELECT FIRST_NAME,
       COUNT(*)
FROM EMPLOYEES
GROUP BY FIRST_NAME
HAVING COUNT(*) > 1;
```

Concept:

```text
GROUP BY column
      ↓
COUNT each value
      ↓
HAVING COUNT(*) > 1
      ↓
Duplicates
```

---

# Analytical / Window Functions

Window functions calculate values using a set of rows **while keeping the original rows**.

### Aggregate vs Window Function

Aggregate:

```sql
SELECT SUM(SALARY)
FROM EMPLOYEES;
```

```text
Many rows
    ↓
Summary
    ↓
Fewer rows
```

Window:

```sql
SELECT FIRST_NAME,
       SALARY,
       SUM(SALARY) OVER()
FROM EMPLOYEES;
```

```text
Many rows
    ↓
Calculation
    ↓
Same rows + calculated value
```

So:

> **Aggregate functions are mainly used for summaries, while window functions give calculations along with the detailed rows.**

---

# 6. `OVER()`

`OVER()` tells SQL:

> **Perform this calculation as a window calculation.**

Example:

```sql
SELECT FIRST_NAME,
       SALARY,
       SUM(SALARY) OVER()
FROM EMPLOYEES;
```

The total salary is calculated, but every employee row remains.

```text
SUM(SALARY)
    ↓
SUM(SALARY) OVER()
    ↓
Window calculation
    ↓
Original rows remain
```

---

# 7. `PARTITION BY`

`PARTITION BY` divides the rows into separate **windows/groups for the calculation**.

Example:

```sql
SELECT FIRST_NAME,
       DEPARTMENT_ID,
       SALARY,
       SUM(SALARY) OVER(
           PARTITION BY DEPARTMENT_ID
       )
FROM EMPLOYEES;
```

Now the salary total is calculated separately for each department.

```text
Department 10
    ↓
Calculate separately

Department 20
    ↓
Calculate separately
```

But the original employee rows remain.

### GROUP BY vs PARTITION BY

```text
GROUP BY
→ creates groups
→ collapses rows
→ produces summary

PARTITION BY
→ creates windows for calculation
→ does NOT collapse rows
→ keeps detailed rows
```

---

# 8. `ORDER BY` Inside `OVER()`

`ORDER BY` inside `OVER()` determines the order used by the window calculation.

Example:

```sql
SUM(SALARY) OVER(
    ORDER BY EMPLOYEE_ID
)
```

This can produce a **running total**:

```text
Employee 1 → 5000
Employee 2 → 12000
Employee 3 → 18000
Employee 4 → 26000
```

So:

```text
OVER()
│
├── PARTITION BY → which rows belong together?
│
└── ORDER BY     → in what order?
```

---

# 9. RANK()

`RANK()` gives a position to rows.

```sql
RANK() OVER(
    ORDER BY SALARY DESC
)
```

Example:

```text
Salary     Rank

490         1
485         2
485         2
470         4
```

**Ties create gaps.**

---

# 10. DENSE_RANK()

`DENSE_RANK()` also gives a position, but **doesn't create gaps**.

```sql
DENSE_RANK() OVER(
    ORDER BY SALARY DESC
)
```

Result:

```text
Salary     Dense Rank

490         1
485         2
485         2
470         3
```

---

# 11. ROW_NUMBER()

`ROW_NUMBER()` gives every row a **unique number**.

```sql
ROW_NUMBER() OVER(
    ORDER BY SALARY DESC
)
```

Result:

```text
Salary     Row Number

490         1
485         2
485         3
470         4
```

### Difference

```text
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

ROW_NUMBER
1
2
3
4
```

---

# 12. LEAD()

`LEAD()` gets a value from the **next row**.

```sql
SELECT EMPLOYEE_ID,
       FIRST_NAME,
       LEAD(FIRST_NAME) OVER(
           ORDER BY EMPLOYEE_ID
       )
FROM EMPLOYEES;
```

Concept:

```text
Current → Next
```

Example:

```text
John  → Alice
Alice → Bob
Bob   → David
David → NULL
```

```text
LEAD = NEXT ROW
```

---

# 13. LAG()

`LAG()` gets a value from the **previous row**.

```sql
SELECT EMPLOYEE_ID,
       FIRST_NAME,
       LAG(FIRST_NAME) OVER(
           ORDER BY EMPLOYEE_ID
       )
FROM EMPLOYEES;
```

Concept:

```text
Previous → Current
```

Example:

```text
John  → NULL
Alice → John
Bob   → Alice
David → Bob
```

```text
LAG = PREVIOUS ROW
```

---

# 14. `PARTITION BY` with Analytical Functions

Example:

```sql
RANK() OVER(
    PARTITION BY DEPARTMENT_ID
    ORDER BY SALARY DESC
)
```

Means:

> Rank employees by salary **separately within each department**.

Similarly:

```sql
LAG(SALARY) OVER(
    PARTITION BY DEPARTMENT_ID
    ORDER BY EMPLOYEE_ID
)
```

Means:

> Get the previous employee's salary **within the same department**.

---

# 🧠 Final TL;DR

```text
AGGREGATE FUNCTIONS
│
├── SUM
├── MIN
├── MAX
├── AVG
└── COUNT
       ↓
   Summary
       ↓
   GROUP BY
       ↓
   Group-level result
```

```text
WINDOW / ANALYTICAL FUNCTIONS
│
├── RANK()       → ranking with gaps
├── DENSE_RANK() → ranking without gaps
├── ROW_NUMBER() → unique row number
├── LAG()        → previous row
├── LEAD()       → next row
└── SUM/AVG/etc. OVER() → calculations while keeping rows
```

```text
OVER()
→ makes the calculation a window calculation

PARTITION BY
→ separates rows into windows for the calculation

ORDER BY
→ controls the order inside the window
```

### The main concept:

> **GROUP BY = summarize the rows.**
> **Window functions = calculate using the rows while still showing the detailed rows.**
