**Spark/PySpark topics, in order:**

**Stage 1: Conceptual foundation (learn this before touching code)**
1. What distributed computing means — why Spark exists, cluster/driver/executor architecture
2. RDDs vs DataFrames vs Datasets — know RDDs exist conceptually, but DataFrames are what you'll actually use
3. Lazy evaluation — transformations vs actions, why it matters
4. Partitions — what they are, how data gets split across a cluster
5. The DAG (Directed Acyclic Graph) — how Spark plans execution

**Stage 2: Core DataFrame operations (the daily-driver syntax)**
6. Creating DataFrames — from CSV/JSON/Parquet, from schemas
7. Basic transformations — select, filter, withColumn, drop
8. Aggregations — groupBy, agg, common functions (sum, avg, count)
9. Joins in Spark — types, and why joins are expensive in distributed systems
10. Window functions in PySpark — same concepts as SQL, different syntax
11. Handling nulls — na.drop, na.fill
12. sort/orderBy

**Stage 3: The "why is my job slow" layer — this is what interviews actually probe**
13. Shuffling — what causes it, why it's expensive, how to minimize it
14. Wide vs narrow transformations — which ones trigger a shuffle
15. Partitioning strategy — repartition vs coalesce, and when to use each
16. Data skew — what it is, how to detect it, how to fix it (salting, etc.)
17. Broadcast joins — when Spark auto-broadcasts, when to force it, why it avoids shuffle
18. Caching/persisting — cache() vs persist(), when it actually helps vs wastes memory
19. Reading the Spark UI / execution plan — explain(), understanding stages and tasks

**Stage 4: File formats and I/O (DE-specific)**
20. Parquet vs CSV vs JSON — why Parquet is preferred (columnar, compression, schema)
21. Schema enforcement — inferSchema vs defining schema explicitly, why explicit is better at scale
22. Partitioned writes — writing data partitioned by column (e.g., by date) for downstream efficiency
23. Handling small files problem — why too many small files hurts performance

**Stage 5: Pipeline-specific patterns**
24. UDFs (User Defined Functions) — how to write them, and why they're slower than built-in functions (serialization overhead)
25. Incremental/batch processing patterns — reading only new data, watermarking (if streaming touches your role)
26. Spark SQL — running SQL directly on DataFrames (temp views)

**Stage 6: Config/tuning awareness (lighter for 2-3 YOE, but good to know exists)**
27. Cluster resource config — num executors, executor memory/cores (conceptual understanding, not deep tuning)
28. spark.sql.shuffle.partitions — common tuning knob people ask about

**Why this order:** Stage 1 concepts (especially lazy eval, partitions, shuffle) are the mental model everything else hangs off — skipping this and jumping straight to syntax is why people can write PySpark code but fail the "why is this slow" interview questions. Stage 3 is where most real interview signal lives for 2-3 YOE — "tell me how you'd debug a slow Spark job" is an extremely common question, and it's unanswerable without Stage 1 + Stage 3 together.