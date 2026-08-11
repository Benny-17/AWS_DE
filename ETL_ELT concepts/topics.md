ETL isn't a separate "tool" like SQL or Spark — it's the connecting concept that ties everything else together. It doesn't get its own stage; it's woven through what you've already been learning. But there are ETL-specific concepts worth calling out on their own:

**ETL/ELT concepts to learn:**

1. **ETL vs ELT** — the difference, why modern warehouses (Redshift/Snowflake/BigQuery) shifted toward ELT
2. **Extract patterns** — full extract vs incremental extract, pulling from APIs/DBs/files
3. **Transform patterns** — cleaning, deduplication, joining, aggregating, type casting (this is where your SQL/Python/Spark skills literally get applied)
4. **Load patterns** — full load vs incremental load, append-only vs upsert/merge
5. **Batch vs streaming ETL** — scheduled batch jobs vs real-time/near-real-time pipelines
6. **Idempotency** — designing pipelines so re-running them doesn't duplicate/corrupt data
7. **Incremental processing** — watermarking, CDC (Change Data Capture), using timestamps/IDs to pull only new data
8. **Data quality checks** — validating data mid-pipeline (nulls, duplicates, schema drift, row count sanity checks)
9. **Error handling & retries** — dead-letter queues, alerting, partial failure handling
10. **Orchestration of ETL** — this is literally Airflow/Step Functions — sequencing extract → transform → load with dependencies
11. **Pipeline design questions** — "design an ETL pipeline that ingests X and loads it into Y" — this is the actual interview format

**Where it fits in your overall prep:**

Think of it like this — SQL, Python, Spark, AWS, and Data Modeling are your **tools and building blocks**. ETL is **how you assemble them into a working pipeline**. So:

- Your Python/Spark skills → power the "Transform" step
- Your AWS skills (S3, Glue, Redshift, Airflow) → power "Extract, Load, and Orchestration"
- Your Data Modeling skills → determine *what* the final Load target looks like

**Practically:** once you're solid on the 5 pillars, ETL shows up as the **system design / pipeline design round** — "walk me through how you'd build a pipeline to ingest daily sales data from an API into Redshift." That question requires pulling from all 5 areas at once. So treat ETL concepts (1-9 above) as a short standalone study block, then spend your practice time doing full pipeline design questions (#11) — that's where it all gets tested together.