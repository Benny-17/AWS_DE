OLTP vs OLAP — the fundamental distinction, why DE cares about OLAP
Fact tables vs dimension tables — what goes where, grain of a fact table
Star schema — structure, why it's the default for analytics
Snowflake schema — how it differs from star, tradeoffs (normalization vs query simplicity)
Surrogate keys vs natural keys — why surrogate keys are preferred
Slowly Changing Dimensions (SCD) — Type 0, 1, 2, 3 (Type 1 and 2 matter most — know them cold)
Granularity/grain — choosing the right grain for a fact table, why it matters
Fact table types — transaction facts, periodic snapshot, accumulating snapshot
Conformed dimensions — sharing dimensions across multiple fact tables/data marts
Normalization basics (1NF/2NF/3NF) — conceptual, mainly to contrast against denormalized warehouse design
Data vault modeling (lighter, good to know exists) — hubs, links, satellites — some companies use this instead of star schema
Designing for a given use case — practice questions like "model an e-commerce order system" or "model a ride-sharing app" — this is where everything above gets applied

Why this order: 1-6 are non-negotiable — SCD Type 2 especially comes up in almost every DE interview, either as a modeling question or as a "write SQL to implement this" question. #12 is the actual interview format most companies use, so once you know 1-9, start practicing full design questions out loud.