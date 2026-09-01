# CS2 Economy: The October Update Impact

![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## About The Project
I built this data pipeline and interactive dashboard to test a specific business hypothesis: did the new update cannibalize the existing market, or did it stimulate it?

## Tech Stack

I wrote a custom ETL script in Python using `pandas` and `SQLAlchemy` to parse raw JSON data from the Steam API, handle timestamps and timezones, clean duplicate transactions, and structure the data. The processed datasets were stored and queried using a PostgreSQL relational database.

For the visualization, I built interactive Tableau dashboards utilizing a Difference-in-Differences (Diff-in-Diff) logic. To verify that volume and revenue shifts were directly caused by the update rather than broader market seasonality, an isolated control item (Printstream) was monitored throughout the analysis.

## Business Context 
Counter-Strike 2 (CS2) has a massive global P2P economy that works like a real-world exchange market. In this project, I treat digital items (skins and cases) as real financial assets. My goal was to use raw market data to analyse how a major product update changed user spending behaviour and the platform's total revenue.

## Key Findings

**$1M Revenue Spike**
The update generated $1M in marketplace commissions post-update within the core cohort, with items like the P90 and M4A1 suddenly capturing the vast majority of the cohort's transaction volume.

**The "Halo Effect"**
The hypothesis of market cannibalization was completely disproved. Without a massive wave of new users, ecosystem-wide case unboxing revenue surged by 98% due to increased economic engagement from the existing player base.

**Luxury Market Panic Selling**
High-tier items like the Butterfly Knife experienced a sudden and temporary price drop. This anomaly was driven by a supply shock and some users panic-selling their assets at a discount to cash out before a perceived market crash.

## Interactive Dashboard

The entire business logic, A/B timeline comparison, and item breakdowns are available on Tableau Public.

[View the Live Dashboard on Tableau Public]( https://public.tableau.com/app/profile/arsen.musaelian/viz/CS2_Market_Economy_Impact/Dashboard1?publish=yes )
