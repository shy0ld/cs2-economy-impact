# CS2 Economy: The October Update Impact

![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## What is this project about?
What happens to an in-game economy when developers suddenly introduce a massive new crafting mechanic? I built this data pipeline and interactive dashboard to test a specific business hypothesis: did the new update cannibalize the existing market, or did it stimulate it?

## Key Findings

**The $1.16M Revenue Boom (Analyzed Cohort)**
Following the update, marketplace commission revenue across our analyzed core asset sample reached $1.16M. Within this studied group, key crafting inputs (P90 and M4A1) emerged as the primary economic drivers, capturing over half of the cohort's total transaction volume.

**The Halo Effect is Real**
The legacy market (case unboxing) did not collapse under the new update. In fact, ecosystem-wide engagement boosted case unboxing revenue by 98%. The hypothesis of direct market cannibalization was disproved.

**Luxury Segment Dynamics: Supply Shock & Liquidity Shift**
High-tier items (such as the Butterfly Knife) experienced a temporary price drop. This was primarily driven by a sudden supply shock as direct knife crafting was enabled, diluting artificial scarcity. This effect was further amplified by a short-term liquidity shift, where players liquidated luxury assets to secure Steam balance for new crafting recipes.

## Tech Stack

This project goes beyond just making charts; it represents a full data processing pipeline from raw files to financial analytics.

I wrote a custom ETL script in Python using `pandas` and `SQLAlchemy` to parse raw JSON data from the Steam API, handle timestamps and timezones, clean duplicate transactions, and structure the data. The processed datasets were stored and queried using a PostgreSQL relational database.

For the visualization, I built interactive Tableau dashboards utilizing a Difference-in-Differences (Diff-in-Diff) logic. To verify that volume and revenue shifts were directly caused by the update rather than broader market seasonality, an isolated control item (Printstream) was monitored throughout the analysis.

## Interactive Dashboard

The entire business logic, A/B timeline comparison, and item breakdowns are available on Tableau Public.

[View the Live Dashboard on Tableau Public]( https://public.tableau.com/app/profile/arsen.musaelian/viz/CS2_Market_Economy_Impact/Dashboard1?publish=yes )
