import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['geopotential'],
        'pressure_level': ['500'],
        'year': [str(y) for y in range(1940, 2025)],
        'month': [
            '01','02','03','04','05','06',
            '07','08','09','10','11','12'
        ],
        'day': [f'{d:02d}' for d in range(1, 32)],
        'time': ['00:00'], 
        'area': [49, -95, 41, -75],   
        'format': 'grib',
    },
    'z500.grib'
)
