# SQL Roadmap: Zero to Pro (for AWS Data Engineer Roles)

A structured path to go from SQL basics to interview-ready, tailored for someone transitioning from DevOps into Data Engineering. Target: 2+ years experience level interviews.

---

## How to Use This Roadmap

- Follow phases in order — don't skip to window functions before joins are second nature.
- Solve problems daily, don't just read syntax.
- After each phase, do 10-15 practice problems before moving on.
- Total time estimate: **3 weeks** if you dedicate 1-2 hrs/day.

---

## Phase 0: Setup & Mental Model (Day 1)

### Get a practice environment
Pick one:
- **PostgreSQL** locally (recommended — closest to what's used in real DE jobs, plus works well with AWS RDS/Redshift syntax)
- **SQLite** via DB Browser (lightweight, zero setup)
- Online: pgexercises.com, or StrataScratch/LeetCode (browser-based, no install)

### Understand the mental model
- A database is a collection of **tables** (rows + columns).
- SQL queries are **declarative** — you describe *what* you want, not *how* to get it (this is different from procedural code you're used to in DevOps scripting).
- Query execution order (important, differs from how you *write* the query):
  ```
  FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
  ```
  Understanding this order explains a LOT of confusing SQL errors later.

---

## Phase 1: Fundamentals (Days 2-5)

### Topics to master
- [ ] `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] Filtering: `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE`, `IS NULL`
- [ ] `DISTINCT`
- [ ] Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- [ ] `GROUP BY` and `HAVING` (the difference between `WHERE` and `HAVING` is a classic interview question)
- [ ] Basic `JOIN` types:
  - `INNER JOIN`
  - `LEFT JOIN` / `LEFT OUTER JOIN`
  - `RIGHT JOIN`
  - `FULL OUTER JOIN`
  - `CROSS JOIN`
  - `SELF JOIN`

### Key concept to nail
**WHERE vs HAVING**
- `WHERE` filters rows *before* grouping.
- `HAVING` filters groups *after* aggregation.
```sql
-- WHERE: filter raw rows
SELECT department, COUNT(*) 
FROM employees
WHERE salary > 50000
GROUP BY department;

-- HAVING: filter grouped results
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

### Practice checkpoint
Solve 15-20 easy problems on joins + aggregations before moving on.

---

## Phase 2: Intermediate — CTEs & Subqueries (Days 6-9)

### Topics to master
- [ ] Subqueries (in `WHERE`, `SELECT`, `FROM`)
- [ ] Correlated vs non-correlated subqueries
- [ ] `CTE` (Common Table Expressions) using `WITH`
- [ ] `UNION` vs `UNION ALL`
- [ ] `EXISTS` vs `IN`

### Why CTEs matter
CTEs make complex queries readable — critical when writing production ETL logic. Think of them like naming intermediate variables in a script instead of one giant nested expression.

```sql
WITH high_earners AS (
    SELECT employee_id, department, salary
    FROM employees
    WHERE salary > 80000
)
SELECT department, COUNT(*) AS count_high_earners
FROM high_earners
GROUP BY department;
```

### Subquery vs Join — when to use which
- Use a **JOIN** when you need columns from both tables in your output.
- Use a **subquery** when you only need to filter/check against another table's data.

---

## Phase 3: Window Functions (Days 10-14) — THE MOST IMPORTANT SECTION

This is the single highest-tested topic for 2+ years experience interviews. Do not rush this section.

### What window functions do
Unlike `GROUP BY` (which collapses rows), window functions let you calculate aggregates **while keeping every row visible**.

```sql
SELECT 
    employee_id, 
    department, 
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg_salary
FROM employees;
```

### Must-know window functions
- [ ] `ROW_NUMBER()` — unique sequential number per row
- [ ] `RANK()` — same value = same rank, gaps after ties
- [ ] `DENSE_RANK()` — same value = same rank, NO gaps after ties
- [ ] `LAG()` / `LEAD()` — access previous/next row's value (huge for time-series/DE work)
- [ ] `SUM() OVER()`, `AVG() OVER()` — running totals, moving averages
- [ ] `FIRST_VALUE()` / `LAST_VALUE()`

### Classic pattern: Deduplication (VERY common DE interview question)
```sql
WITH ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM orders
)
SELECT * FROM ranked WHERE rn = 1;
```
This finds the most recent order per customer — a pattern you'll use constantly in real pipelines.

### Classic pattern: Running total
```sql
SELECT 
    order_date, 
    revenue,
    SUM(revenue) OVER (ORDER BY order_date) AS running_total
FROM daily_sales;
```

### Practice checkpoint
Do NOT move to Phase 4 until you can write `ROW_NUMBER()` + `PARTITION BY` deduplication logic without looking it up.

---

## Phase 4: Advanced / Data-Engineer-Specific (Days 15-18)

### Topics to master
- [ ] `CASE WHEN` for conditional logic / pivoting data
- [ ] Date/time functions (`DATE_TRUNC`, `EXTRACT`, `DATEDIFF`, `DATE_ADD`) — heavily used in ETL
- [ ] Handling `NULL`s properly: `COALESCE()`, `NULLIF()`
- [ ] String functions: `CONCAT`, `SUBSTRING`, `TRIM`, `SPLIT_PART`
- [ ] `PIVOT`/manual pivoting using `CASE WHEN` + aggregation
- [ ] Set operations: `UNION`, `INTERSECT`, `EXCEPT`/`MINUS`

### Pivoting example (turning rows into columns)
```sql
SELECT 
    product_id,
    SUM(CASE WHEN month = 'Jan' THEN sales ELSE 0 END) AS jan_sales,
    SUM(CASE WHEN month = 'Feb' THEN sales ELSE 0 END) AS feb_sales
FROM monthly_sales
GROUP BY product_id;
```

### Handling NULLs (common gotcha)
```sql
SELECT COALESCE(phone_number, 'N/A') AS phone
FROM customers;
```

---

## Phase 5: Query Optimization & Execution Plans (Days 19-21)

You won't be asked to be a DBA, but at 2+ YOE you should be able to talk intelligently about performance.

### Topics to know
- [ ] What an index is and how it speeds up lookups
- [ ] `EXPLAIN` / `EXPLAIN ANALYZE` — read a basic query plan
- [ ] Why `SELECT *` is bad practice in production
- [ ] Difference between clustered and non-clustered indexes (conceptual, not deep DBA-level)
- [ ] Why too many indexes slow down writes
- [ ] Partitioning tables (especially relevant for Redshift — distribution keys & sort keys)

### Redshift-specific (since you're targeting AWS DE roles)
- [ ] `DISTKEY` — how data is distributed across nodes
- [ ] `SORTKEY` — how data is physically ordered on disk
- [ ] Why choosing the right DISTKEY/SORTKEY matters for JOIN performance at scale

---

## Cheat Sheet: Interview-Ready Concepts Summary

| Concept | One-liner explanation |
|---|---|
| WHERE vs HAVING | WHERE filters rows before grouping, HAVING filters after |
| INNER vs LEFT JOIN | INNER returns matches only, LEFT returns all from left table + matches |
| RANK vs DENSE_RANK | RANK leaves gaps after ties, DENSE_RANK doesn't |
| Subquery vs JOIN | JOIN when you need columns from both tables, subquery for filtering/checks |
| UNION vs UNION ALL | UNION removes duplicates, UNION ALL keeps them (and is faster) |
| CTE vs Subquery | CTE is more readable, reusable within the same query |
| Clustered index | Physically sorts the table data itself (only one per table) |

---

## Practice Resources (pick 1-2, don't scatter across many)

- **StrataScratch** — real interview questions from actual companies, great for DE-style problems
- **LeetCode SQL** — structured Easy → Medium → Hard progression
- **Mode Analytics SQL Tutorial** — free, especially good for window functions
- **pgexercises.com** — free, PostgreSQL-based, good for fundamentals

---

## Daily Practice Routine

1. Solve 3-5 problems.
2. For each, write the query — then explain out loud *why* you chose that approach (this is literally what interviewers ask).
3. Every 3 days, redo problems you got wrong earlier — repetition beats volume.
4. Once you finish Phase 3 (window functions), start mixing in AWS Redshift/Athena-flavored SQL practice, since syntax has minor differences from standard PostgreSQL.

---

## Self-Check: Are You Interview-Ready?

You should be able to do all of these **without looking anything up**:

- [ ] Write a query with 3+ table joins
- [ ] Deduplicate rows using `ROW_NUMBER()` + `PARTITION BY`
- [ ] Write a running total using window functions
- [ ] Explain WHERE vs HAVING in one sentence
- [ ] Explain RANK vs DENSE_RANK with an example
- [ ] Pivot data using `CASE WHEN` + `SUM()`
- [ ] Read a basic `EXPLAIN` output and identify a full table scan
- [ ] Explain what a DISTKEY/SORTKEY does in Redshift

If you can check all of these off, you're ready to move to the next stack item (Python for data work).

---

*Next step after this: Python for data engineering (pandas, boto3, file/API handling).*