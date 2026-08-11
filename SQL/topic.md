**Stage 1: Foundations (get fluent first)**
1. Basic querying — SELECT, WHERE, GROUP BY, HAVING, ORDER BY
2. Joins — all types
3. NULL handling
4. CASE statements
5. Date/time functions
6. String functions

**Stage 2: The interview-heavy stuff**
7. Subqueries (correlated vs non-correlated)
8. CTEs (including recursive)
9. Window functions — spend real time here, this is the single highest-leverage topic
10. Deduplication techniques (ROW_NUMBER + partition)
11. Set operations (UNION, INTERSECT, EXCEPT)

**Stage 3: Apply what you know to real patterns**
12. Common problem patterns — gaps and islands, sessionization, top-N per group, running totals
(This is where #1-11 come together — don't skip straight here, you'll be lost)

**Stage 4: Aggregation edge cases + shaping data**
13. GROUPING SETS/ROLLUP/CUBE
14. Pivoting/unpivoting

**Stage 5: Data engineering-specific SQL**
15. MERGE/UPSERT (idempotent writes)
16. SCD Type 2 logic in SQL
17. Data cleaning at scale (dupes, malformed data, type mismatches)

**Stage 6: Performance/internals (do this once queries feel natural)**
18. Indexes + EXPLAIN plans
19. How joins execute internally (hash/merge/nested loop)
20. Partitioned tables, predicate pushdown

**Stage 7: Nice-to-have / warehouse-specific**
21. Views vs materialized views
22. Stored procedures/functions
23. Transactions/ACID (conceptual)
24. Constraints (conceptual, feeds into data modeling)

**Why this order:** window functions (stage 2) are useless to practice until joins/CTEs are solid, and the "gaps and islands / sessionization" pattern group (stage 3) is literally window functions + CTEs applied — so it acts as your practice ground and forces synthesis of everything before it. Performance/internals (stage 6) is more valuable once you've written enough queries to actually feel *why* a query is slow.

Realistic pace: Stage 1-3 is the meat — spend 60-70% of your prep time there.

**SQL topics for DE interviews:**

1. Basic querying — SELECT, WHERE, GROUP BY, HAVING, ORDER BY
2. Joins — inner, left/right, full outer, self join, cross join, anti-join
3. Window functions — ROW_NUMBER, RANK, DENSE_RANK, LAG/LEAD, NTILE, running totals, partition by
4. CTEs — including recursive CTEs
5. Subqueries — correlated vs non-correlated
6. Set operations — UNION, UNION ALL, INTERSECT, EXCEPT
7. Aggregations — with GROUP BY edge cases (multiple grouping levels, GROUPING SETS/ROLLUP/CUBE)
8. String functions — parsing, splitting, pattern matching (LIKE, REGEXP)
9. Date/time functions — date diff, truncation, formatting, timezone handling
10. NULL handling — COALESCE, NULLIF, NULL in joins/aggregates
11. CASE statements
12. Query optimization — indexes, EXPLAIN plans, reading query execution order
13. Deduplication techniques — ROW_NUMBER + partition, DISTINCT ON
14. Pivoting/unpivoting data
15. Data types and casting
16. Constraints — primary key, foreign key, unique (conceptual, for modeling)
17. Transactions — ACID basics, isolation levels (conceptual)
18. Common problem patterns — gaps and islands, sessionization, top-N per group, running/cumulative calculations

Master #2, #3, #7, and #18 — those show up in almost every SQL round.

That covers the core, but a few more worth adding depending on how deep the interview goes:

19. **Query performance/internals** — how joins execute (hash join, merge join, nested loop), when indexes help/hurt, query plan cost estimation
20. **Views vs materialized views** — differences, when to use each
21. **Stored procedures/functions** — basics, especially if the company uses Redshift/Snowflake heavily
22. **Handling large-scale query patterns** — partitioned tables, predicate pushdown, avoiding full table scans
23. **Slowly Changing Dimension queries in SQL** — writing SQL to detect changes, implement SCD Type 2 logic
24. **Idempotent SQL writes** — MERGE/UPSERT statements, ON CONFLICT handling
25. **Data cleaning in SQL** — handling duplicates, malformed data, type mismatches at scale

**Honest take:** #1-18 from before is what you'll actually be tested on in 80%+ of interviews. #19-25 are the "if this comes up, don't look clueless" tier — more relevant once you're doing warehouse-specific work (Redshift/Snowflake/BigQuery) or interviewing at a company with heavier data volumes.

Don't try to master all 25 before starting practice. Get solid on window functions, joins, and the "gaps and islands / sessionization / top-N" pattern group first — those are disproportionately common — then layer in the rest.


