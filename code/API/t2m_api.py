import cdsapi

c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-single-levels",
    {
        "product_type": ["reanalysis"],
        "variable": ["2m_temperature"],
        "year": [str(y) for y in range(1940, 2026)],
        "month": [f"{m:02d}" for m in range(1, 13)],
        "day": [f"{d:02d}" for d in range(1, 32)],
        "time": ["12:00"],

        "area": [49, -95, 41, -75],

        "grid": [0.25, 0.25],

        "format": ["grib"],
    },
    "t2m.grib",
)
