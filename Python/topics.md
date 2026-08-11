**Python topics for DE interviews (2-3 YOE):**

**Stage 1: Core language fluency**
1. Data types — lists, tuples, dicts, sets, and when to use each
2. String manipulation — slicing, formatting (f-strings), split/join, regex basics
3. Control flow — loops, comprehensions (list/dict/set comprehensions)
4. Functions — args/kwargs, default params, *args/**kwargs, lambda
5. Error handling — try/except/finally, custom exceptions
6. File I/O — reading/writing CSV, JSON, text files
7. Modules/packages — imports, virtual envs, pip basics

**Stage 2: Data-handling libraries (the DE bread and butter)**
8. Pandas — dataframes, filtering, groupby, merge/join, apply, handling nulls, reading/writing various formats
9. JSON/XML parsing — nested structures, flattening
10. datetime module — parsing, timezone handling, formatting

**Stage 3: OOP (asked more than people expect)**
11. Classes, objects, `__init__`
12. Inheritance, polymorphism basics
13. Decorators — especially since Airflow/pipeline code uses these constantly
14. Generators/iterators — `yield`, memory efficiency, lazy evaluation (this connects directly to how Spark thinks too)

**Stage 4: Automation/scripting patterns for DE**
15. Working with APIs — requests library, pagination, handling rate limits/retries
16. Working with AWS SDK — boto3 basics (S3 read/write, triggering Lambda, etc.)
17. Logging — proper logging vs print statements
18. Environment/config management — reading env vars, config files, secrets handling (conceptually)
19. Writing idempotent/retryable scripts — important for pipeline reliability

**Stage 5: Code quality + interview-specific**
20. Time/space complexity basics (Big O) — expect at least light DSA questions
21. Common DSA patterns — array/string manipulation, dictionaries for counting/grouping, two pointers — DE interviews rarely go deep into DSA like SWE roles, but expect easy-medium LeetCode-style questions
22. Writing modular/testable code — functions with single responsibility
23. Unit testing — pytest basics, mocking

**Stage 6: Nice-to-have**
24. Multithreading/multiprocessing (conceptual — parallel vs concurrent)
25. Context managers — `with` statements, writing your own

**Order logic:** Stage 1-2 is what actually gets tested in take-home/pipeline-writing rounds — prioritize pandas hard since it's the most commonly asked practical skill. Stage 3's generators/decorators matter more than people think because they show up in Airflow DAG code and connect conceptually to Spark's lazy evaluation (which you'll hit next). Stage 5's DSA is usually a *separate, easier* round — don't over-invest, but don't skip either since even easy-medium questions trip people up cold.