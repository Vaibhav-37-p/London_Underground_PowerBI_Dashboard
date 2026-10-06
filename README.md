# London Underground Station Analysis

A transport-data portfolio project exploring station entries and exits using TfL annual-count workbooks. The corrected analysis uses **2007–2017 historical sheets** and **2021 London Underground-only records**.

## Dashboard preview

![London Underground station analysis](London_Underground_Dashboard.png)

[Download the dashboard PDF](London_Underground_Dashboard.pdf)

This repository originated as a Power BI portfolio project. **The current PNG and PDF are static previews regenerated with Python/Matplotlib from the included source workbooks.** They do not contain working filters. No editable Power BI `.pbix` or `.pbip` model is included, so the original DAX and report interactions cannot be inspected here.

## Verified 2021 findings

| Measure | Result | Definition |
|---|---:|---|
| Annualised station entries + exits | **1,180,585,837.77** | Sum of `En/Ex` where `Mode = LU` |
| Underground stations | **270** | Distinct NLC identifiers in the LU subset |
| Busiest Underground station | **King's Cross St. Pancras** | Highest LU-only annualised station count |
| Busiest station count | **36,734,085.14** | Annualised entries + exits |
| Stratford LU-only count | **29,106,619.05** | LU row only; other modes excluded |

**Business takeaway:** Station rankings can help identify locations to investigate for capacity and service planning. These annualised figures alone do not establish platform crowding, peak-hour demand or required staffing levels.

The verified historical totals generally rise across 2007–2016, with a small decline in 2017. Coverage and estimation methods vary; the chart should not be read as a like-for-like panel of identical stations.

## Source selection and important corrections

The original preview mixed incompatible figures. The corrected version follows the original workbooks:

- **2021:** Read the `Annualised` sheet in `AC2021_AnnualisedEntryExit.xlsx`, filter `Mode = LU`, and use the published `En/Ex` field without multiplying it again.
- **2007–2017:** Read each annual sheet in `multi-year-station-entry-and-exit-figures.xls`. Keep station rows with numeric NLC identifiers and numeric values in the annual-total column. Convert the published millions to counts. Exclude headings and total/footer rows.
- **2018–2020:** These years are present in the derived `TfL_stations.csv`, but their original annual-count workbooks are not supplied. The derived CSV combines modes at some interchanges, so these years are omitted from the corrected preview rather than silently treated as LU-only. The chart shows a gap, not zeros or interpolation.
- The previous **24.72B total**, **1.77B average**, station ranking and zone shares have been removed from the current preview because they did not reconcile with the selected sources.
- Stratford's previous **63.44M** figure combines LU, Overground, DLR and TfL Rail rows in the 2021 workbook. It is not an Underground-only station figure.

## Metric definitions and limitations

- **Entries + exits** are station movements, not unique passengers or unique journeys. A journey can contribute an entry at one station and an exit at another.
- The workbook notes describe annualisation from typical-day counts and associated factors. These are not a simple count of every passenger event during a calendar year.
- The historical workbook and the 2021 workbook use different source structures and annualisation conventions. Avoid interpreting their difference as a precise like-for-like percentage change.
- Station coverage changes by year. The reproduction outputs include the number of contributing station rows for each year.
- The old combined CSV and geographic files are retained as source material, but they do not control the revised totals or rankings. The revised preview does not claim verified zone or geographic analyses.

## Data sources

- [TfL open-data information](https://tfl.gov.uk/info-for/open-data-users/our-open-data)
- [TfL crowding and annual-count data portal](https://crowding.data.tfl.gov.uk/)
- [Historical annual workbook](multi-year-station-entry-and-exit-figures.xls)
- [2021 annualised workbook](AC2021_AnnualisedEntryExit.xlsx)

The calculations use the exact workbook copies in this repository. Retain TfL attribution and consult the publisher's reuse terms when redistributing source data.

## Reproduce the preview

```bash
python -m pip install -r requirements.txt
python rebuild_preview.py
```

The script reads the workbooks, checks station-ID uniqueness, writes the verified tables and rebuilds the PNG/PDF. It requires no Power BI installation.

## Repository files

| File | Purpose |
|---|---|
| `London_Underground_Dashboard.png` / `.pdf` | Corrected static preview |
| `rebuild_preview.py` / `requirements.txt` | Reproducible calculations and rendering |
| `verified_annual_totals.csv` | Annual totals and contributing station counts |
| `verified_2021_stations.csv` | Full LU-only 2021 station ranking |
| `multi-year-station-entry-and-exit-figures.xls` | Original 2007–2017 workbook |
| `AC2021_AnnualisedEntryExit.xlsx` | Original 2021 workbook, including source notes |
| `TfL_stations.csv` | Legacy combined dataset; not used for corrected totals |
| `Stations_20220221.csv`, `lu_lines.geojson`, `night_tube.geojson` | Supporting geographic files |

## Skills demonstrated

Data validation · Excel data extraction · Metric definitions · Ranking · Time-series presentation · Reproducible Python analysis · Data storytelling

**Vaibhav Panchal**
