# London Underground Power BI Dashboard

A Power BI portfolio project exploring London Underground station entries and exits from **2007 to 2021**, using Transport for London (TfL) open data.

![London Underground Dashboard](images/london-underground-dashboard.png)

## Project Overview

The goal of this project is to turn historic London Underground station usage data into a clear, interactive dashboard that highlights long-term passenger trends, the busiest stations, geographic patterns and station distribution across the network.

The dashboard is designed to demonstrate practical data-analysis skills including data preparation, KPI design, trend analysis, ranking, geographic visualisation and business-focused storytelling in Power BI.

## Dashboard Highlights

- **24.72B** total station entries and exits across 2007–2021
- **1.77B** average annual entries and exits
- **Stratford** was the busiest station in 2021 with **63.44M** entries and exits
- **270** London Underground stations represented in the station dataset
- Passenger activity increased through 2019 before falling sharply in 2020 during the COVID-19 period
- 2021 showed a partial recovery compared with 2020

## Dashboard Features

The dashboard includes:

- Year, station, line, zone, network type and Night Tube filters
- Total entries and exits KPI
- Average annual entries KPI
- Busiest station KPI
- Total stations KPI
- Entries and exits trend from 2007–2021
- Top 5 and Top 10 station rankings
- Station distribution by zone
- Geographic station activity map
- Key insight cards summarising the main findings

## Tools & Skills

- **Power BI** – dashboard design and visualisation
- **Power Query** – data cleaning and transformation
- **DAX** – measures and KPI calculations
- **Excel / CSV** – source data handling
- **Data Modelling** – joining station, usage and geographic data
- **Data Storytelling** – translating transport data into clear insights

## Repository Structure

```text
London_Underground_PowerBI_Dashboard/
├── data/
│   ├── multi-year-station-entry-and-exit-figures.xlsx
│   ├── AC2021_AnnualisedEntryExit.xlsx
│   ├── TfL_stations.csv
│   ├── Stations_20220221.csv
│   ├── lu_lines.geojson
│   └── night_tube.geojson
├── images/
│   └── london-underground-dashboard.png
└── README.md
```

## Data Source

Source data: **Transport for London (TfL) Open Data / London Underground station entry and exit data**.

The repository includes the source files used for the portfolio analysis. Please refer to TfL's data terms and conditions when reusing or redistributing the data.

## Key Insights

1. Underground station activity generally increased between 2007 and 2019.
2. Usage fell substantially in 2020, reflecting the impact of the COVID-19 pandemic on travel.
3. 2021 showed a recovery from 2020 levels, although activity remained below 2019.
4. Stratford recorded the highest station entries and exits in 2021.
5. Central London and major interchange stations account for many of the network's highest passenger volumes.

## About This Project

This project was created as part of my data analytics portfolio to demonstrate how Power BI can be used to analyse real-world public transport data and communicate useful insights through an accessible dashboard.

---

If you found this project useful, feel free to star the repository or connect with me on LinkedIn.
