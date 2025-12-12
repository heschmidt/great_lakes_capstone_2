import cdsapi

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "format": "netcdf",
        "product_type": "monthly_averaged_reanalysis",
        "variable": "2m_temperature",
        "year": [str(y) for y in range(1940, 2025)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "time": "00:00",
    },
    "era5_t2m_global_monthly_1940_2024.nc"
)
