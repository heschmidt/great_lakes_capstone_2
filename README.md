# GREAT_LAKES_CAPSTONE_2  
**Event-Scale Characteristics and Drivers of Cold Air Outbreaks over the Great Lakes**

**Author:** Haley Schmidt  
**Program:** M.S. Weather & Climate Risk and Data Analytics, UIUC  
**Capstone Project**

---

## Project Overview

This project develops an event-based climatology of Cold Air Outbreaks (CAOs) over the Great Lakes region using ERA5 reanalysis data. CAOs are identified as persistent, multi-day cold events rather than isolated daily anomalies, allowing for analysis of their frequency, duration, intensity, spatial coverage, synoptic structure, and climate drivers.

The study evaluates the relative roles of:
- Regional contrasts (north/south, upwind/downwind, lakefront/inland)
- Climate teleconnections (ENSO, PDO, AO, NAO)
- Arctic Amplification (AA)

---

## Data Sources

### ERA5 Reanalysis (ECMWF)
Variables:
- 2-m air temperature (T2m)
- Mean sea level pressure (MSLP)
- 500-hPa geopotential height (Z500)

Resolution:
- Spatial: 0.25°
- Temporal: Daily (monthly for Arctic Amplification)

### Teleconnection Indices (NOAA CPC)
- ENSO (Niño-3.4)
- Pacific Decadal Oscillation (PDO)
- Arctic Oscillation (AO)
- North Atlantic Oscillation (NAO)

---

## Cold Air Outbreak (CAO) Definition

A Cold Air Outbreak is defined as:
- Daily T2m below the 5th percentile of DJF temperatures
- Threshold computed independently for each grid cell
- Minimum duration of 3 consecutive days
- Contiguous CAO days grouped into discrete events

Event metrics include:
- Duration (days)
- Intensity (area-weighted mean temperature anomaly)
- Spatial coverage (% of domain affected)
- Composites (T2m, MSLP, Z500)

---

## Output Files

- `events_df.csv` – individual CAO events and metrics  
- `cao_summary.csv` – seasonal CAO statistics  
- `regional_metrics_df.csv` – subdomain-specific metrics  
- `tele_leads_djf.csv` – lagged teleconnection indices  
- `event_summary_by_cluster.csv` – k-means teleconnection regimes  
- `trends_summary.csv` – Mann–Kendall and Sen’s slope results  

---

## Software and Libraries

- Python 3.9+
- xarray
- numpy
- pandas
- matplotlib
- cartopy
- seaborn
- scipy
- pymannkendall
- scikit-learn

