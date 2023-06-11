import numpy as np
import pandas as pd

start_date = pd.to_datetime('2022-01-01 08:00:00')
num_records = 1000
dates = pd.date_range(start_date,periods=num_records, freq='10min')

cycles = np.arange(10,10+num_records)
temperature = np.random.uniform(25.0,26.0, num_records)
pressure = np.random.uniform(99.5, 100.5, num_records)

data = pd.DataFrame({'date':dates, 'cycles':cycles, 'temperature':temperature, 'pressure':pressure})

data.to_csv('sensory_synthetic', index= False)
